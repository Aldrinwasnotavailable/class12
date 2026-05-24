import csv

ITEMTOSEARCH = input("Enter Item Number to search: ")

with open(r'd:\Aldrin\Python\Class12\itemnew.csv', 'r', encoding='utf-8', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["ITEMNO"] == ITEMTOSEARCH:
            print(f"Item found: {row['ITEM']}")
            break