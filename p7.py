#Wap to create a binary file and append some records to this binary file

import pickle

def append_records(filename):
    try:
        with open(filename, 'ab') as file:
            n = int(input("Enter the number of recorsd to append"))
            for _ in range(n):
                name = input("Enter name: ")
                roll_no = input("Enter roll no: ")
                record = {'name': name, 'roll_no': roll_no}
                pickle.dump(record, file)
        print("Records appended successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")