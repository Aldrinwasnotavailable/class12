# Create a binary file with name and roll no. Search for a particular name and display the roll no.,if not found display appropriate message.
import pickle

def create_file(filename):
    records = []
    n = int(input("Enter number of records to add: "))
    for _ in range(n):
        name = input("Enter name: ")
        roll_no = input("Enter roll no: ")
        records.append({'name': name, 'roll_no': roll_no})
    
    with open(filename, 'wb') as file:
        pickle.dump(records, file)
    print("Records added successfully.")

def search_name(filename, search_name):
    try:
        with open(filename, 'rb') as file:
            records = pickle.load(file)
            for record in records:
                if record['name'] == search_name:
                    print(f"Roll No. of {search_name} is {record['roll_no']}.")
                    return
            print(f"{search_name} not found.") 
    except FileNotFoundError:
        print("File not found. Please create the file first.")