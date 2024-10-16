import sqlite3
import pandas as pd

with sqlite3.connect(r"C:\Users\marco\Documents\powerbi-python\Scripts\car_sales.db") as connection:
    df = pd.read_sql_query("SELECT * FROM sales", connection)
# cars
cars = df[
    [
        "vin",
        "car",
        "mileage",
        "license",
        "color",
        "purchase_date",
        "purchase_price",
        "investment",
    ]
]
# Customer and Sales
customers = df[["vin", "customer"]]
sales = df[["vin", "sale_price", "sale_date"]]