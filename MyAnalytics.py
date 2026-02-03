import pandas as pd
from datetime import datetime



df=pd.read_csv("products.csv")[:20]
print(df)


# print(datetime.)


# data=df["product_category"]
# print(data)

# # filter products by Electronics
# electronic=df[df["product_category"]=="Electronics"]
# print(electronic)




# once we have dataframe available 
    #   subscript gives us column






# filter products by Electronics having price > 100


# display price of products 
# electronic_price=df[df["product_category"]=="Electronics"]["product_price"]
# print(electronic_price)

# electronic_price=df[df["product_category"]=="Electronics"][["product_id","product_category","product_price"]]
# print(electronic_price)

# data=electronic_price_three_hundred[electronic_price["product_price"]>300]
# print(data)




# electronic_price=df[df["product_price"]>100 and df["product_category"]=="Electronics"].all()[["product_id","product_category"]]
# print(electronic_price)

# display only product_category as "Food"  and manufacturing date


# data=df[df["product_category"]=="Food"]      [["product_id","product_category","product_manufacturing_date"]]
# print(data)


# find the products with price greater than 300

# group by categories and calculate their average price


# find products having expiry date 30 days from today



today=datetime.now()
print("today's Value",today)
print("today's Value",type(today))
print("type of timedelta",type(pd.Timedelta(days=30)))
after_thirty_days=today+pd.Timedelta(days=30)
print(type(after_thirty_days))
print("date after 30 days",after_thirty_days)


# display the expiry date of electronic
#          where clause
# data=df[df["product_category"]=="Electronics"][["product_id","product_expiry_date"]]
# print(data)

# select product_id,product_expiry_date from product where "product_category"="Electronics"




df["product_expiry_date"]=pd.to_datetime(df["product_expiry_date"])
expiring_soon=df[(df["product_expiry_date"]>=today) & (df["product_expiry_date"]<=after_thirty_days)]
print(expiring_soon)



# Calculate the self life of product{ difference between mfg and expoey date}

# create a pivot table showing count of product categorywise



# product_with_price_above_300 =df[df["product_price"]>300][["product_id","product_category","product_price"]]

# print(product_with_price_above_300)

# group_by_product=df.groupby('product_category')['product_price'].agg(['mean','min','max','count'])
# print(group_by_product)

# any() and all functions, conditional statements, chaining


# checking if any value meets the condition
# df[df["product_category"]=="Food"]     # select * from product where product_category="Food"

# df[df["product_category"]=="Food"]            [["product_id","product_category"]]




# print(f"Any product_price > 1500,{(df["product_price"]>1500).any()}")

# check all values to meet the condition

# if all values are greater than 500
# print(f"Any product_price > 500,{(df["product_price"]>5).all()}")



# AND
# products price greater than 1000 and being  ELecteronics



# condition1=df["product_price"]>=100
# condition2=df["product_category"]=="Electronics"
# condition3=df["product_category"]=="Food"

# print(f"Expensive Electronics{(condition1 & condition2 & condition3).any()}")

# avg=df["product_price"].mean()
# print("Average",avg)


# df1=df.copy()

# avg_group=df.groupby("product_category")['product_price'].transform('mean')

# print("Avergae group",avg_group)

# comp_df=df.copy()
# comp_df["category_avge"]=avg_group


# above_average_group=comp_df[comp_df["product_price"]>comp_df["category_avge"]] 
# print("comp",above_average_group)


# group_by_mfg_date=df.groupby("product_manufacturing_date")['product_price']

# above_avg_group=df1[df1["product_price"]>df1[]




# Enter A date
# Enter a city, state of US
# use weatherapi to find rain on that day any time and check it with your time did it rain at the same time in your place
