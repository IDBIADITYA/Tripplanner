import requests
import json
from faker import Faker
import random

fake = Faker()
BASE_URL = "http://localhost:8114/api"

def populate_authors():
    """Populate Author table"""
    print("\n=== Populating Authors ===")
    url = f"{BASE_URL}/authors/"
    author_ids = []

    for i in range(20):
        name = fake.name()
        data = {
            "name": name,
            "email": fake.email(),
            "bio": fake.text(max_nb_chars=200),
            "birthdate": fake.date_of_birth(minimum_age=25, maximum_age=80).strftime('%Y-%m-%d')
        }

        try:
            response = requests.post(url, json=data)
            if response.status_code in [200, 201]:
                author_id = response.json()['id']
                author_ids.append(author_id)
                print(f"[OK] Created author {i+1}: {name} ({data['email']})")
            else:
                print(f"[ERROR] Error: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"[ERROR] Exception: {e}")

    return author_ids

def populate_books(author_ids):
    """Populate Book table"""
    print("\n=== Populating Books ===")
    url = f"{BASE_URL}/books/"

    for i in range(20):
        data = {
            "author": random.choice(author_ids),
            "title": fake.catch_phrase()
        }

        try:
            response = requests.post(url, json=data)
            if response.status_code in [200, 201]:
                print(f"[OK] Created book {i+1}: {data['title']}")
            else:
                print(f"[ERROR] Error: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"[ERROR] Exception: {e}")

def populate_courses():
    """Populate Course table"""
    print("\n=== Populating Courses ===")
    url = f"{BASE_URL}/courses/"
    course_ids = []

    courses = [
        "Web Development", "Data Science", "Machine Learning", "Mobile Development",
        "Cloud Computing", "Cybersecurity", "DevOps", "Blockchain",
        "AI Engineering", "Database Management", "UI/UX Design", "Network Engineering",
        "Game Development", "IoT", "Quantum Computing", "AR/VR Development",
        "Software Testing", "System Design", "Embedded Systems", "Digital Marketing"
    ]

    for i in range(20):
        data = {
            "name": courses[i]
        }

        try:
            response = requests.post(url, json=data)
            if response.status_code in [200, 201]:
                course_id = response.json()['id']
                course_ids.append(course_id)
                print(f"[OK] Created course {i+1}: {data['name']}")
            else:
                print(f"[ERROR] Error: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"[ERROR] Exception: {e}")

    return course_ids

def populate_students(course_ids):
    """Populate Student table"""
    print("\n=== Populating Students ===")
    url = f"{BASE_URL}/students/"

    for i in range(20):
        # Each student enrolled in 1-4 random courses
        num_courses = random.randint(1, min(4, len(course_ids)))
        selected_courses = random.sample(course_ids, num_courses)

        data = {
            "name": fake.name(),
            "course": selected_courses
        }

        try:
            response = requests.post(url, json=data)
            if response.status_code in [200, 201]:
                print(f"[OK] Created student {i+1}: {data['name']} (enrolled in {num_courses} courses)")
            else:
                print(f"[ERROR] Error: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"[ERROR] Exception: {e}")

def populate_teamdc():
    """Populate TeamDC table"""
    print("\n=== Populating TeamDC ===")
    url = f"{BASE_URL}/teamdc/"

    for i in range(20):
        data = {
            "player_name": fake.name(),
            "player_height": round(random.uniform(5.5, 6.8), 2),
            "palyer_weight": round(random.uniform(150, 250), 2),
            "player_matches_played": random.randint(0, 100)
        }

        try:
            response = requests.post(url, json=data)
            if response.status_code in [200, 201]:
                print(f"[OK] Created player {i+1}: {data['player_name']}")
            else:
                print(f"[ERROR] Error: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"[ERROR] Exception: {e}")

def main():
    print("=" * 60)
    print("Starting Data Population")
    print("=" * 60)
    print("\nNote: Profile table requires users to be created manually via Django admin")
    print("Skipping Profile population. Please create users first if needed.\n")

    # Populate authors and get their IDs
    author_ids = populate_authors()

    # Populate books with author references
    if author_ids:
        populate_books(author_ids)
    else:
        print("WARNING: Skipping books - no authors created")

    # Populate courses and get their IDs
    course_ids = populate_courses()

    # Populate students with course references
    if course_ids:
        populate_students(course_ids)
    else:
        print("WARNING: Skipping students - no courses created")

    # Populate TeamDC
    populate_teamdc()

    print("\n" + "=" * 60)
    print("Data Population Complete!")
    print("=" * 60)

if __name__ == "__main__":
    main()
