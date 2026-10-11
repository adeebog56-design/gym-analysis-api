# Importing requiered modules

import pandas as pd
import sqlite3

# Importing database

print("==========Importing database==========")

df = pd.read_csv("Database/gym_members.csv")
df["attendance_status"] = df["attendance_status"].map({
    "Absent":0,
    "Present":1
})

print("Loaded properly...")

# Basic data analysis and operations

print("==========Basic data analysis and operations==========")
print()

print("First few rows \n")
print(df.head())
print()

print("Basic satisitics\n")
print(df.describe())
print()

print("Basic information\n")
df.info()
print()

print("Removing unecessary columns...")
df = df.drop(columns=["visit_date","check_in_time"])
print("Removed successfully...")
print()

print(df.duplicated().sum())

# Value counts

print("==========Value counts==========")
print()

print(df.value_counts(["gender"]))
print()

print(df.value_counts(["membership_type"]))
print()

print(df.value_counts(["workout_type"]))
print()

# Making SQL databse and preprocessed cs file

print("==========Making SQL databse==========")

df.to_csv("Database/Processed_database.csv", index=False)

connection = sqlite3.connect("gym_databse.db")

df.to_sql("gym_members", connection, if_exists = "replace", index=False)

connection.close()

print("Done Propely...")
print()

print("==========END==========")
