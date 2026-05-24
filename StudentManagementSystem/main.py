import mysql.connector

mycon = mysql.connector.connect(host="localhost", user="root", passwd="", database="sms")
cur = mycon.cursor()


def add():
    r = int(input("Enter the roll no: "))
    n = input("Enter the name: ")
    cl = input("Enter the class: ")
    tup = (r, n, cl)
    st = f"INSERT INTO students (rno, name, class) VALUES {tup}"
    cur.execute(st)
    mycon.commit()
    print("student added succesfully")


def remove():
    r = int(input("Enter the roll no: "))
    st = f"DELETE FROM students WHERE rno = {r}"
    cur.execute(st)
    mycon.commit()
    print("student removed succesfully")


def view():
    cur.execute("SELECT * FROM students")
    data = cur.fetchall()
    for row in data:
        print(row)


def modify():
    n = input("Enter the current name of the student: ").strip()
    new_name = input("Enter new name: ").strip()
    new_class = input("Enter new class: ").strip()
    new_roll = int(input("Enter new roll no: "))
    st = "UPDATE students SET name=%s, class=%s, rno=%s WHERE name=%s"
    cur.execute(st, (new_name, new_class, new_roll, n))
    mycon.commit()
    print("Student details updated successfully!\n")


if mycon.is_connected():
    while True:
        print("=" * 50)
        print(" " * 10 + "🎓 STUDENT MANAGEMENT SYSTEM 🎓")
        print("=" * 50)
        print("\nPlease choose an option:\n")
        print(" [1] ➤ ADD STUDENT")
        print(" [2] ➤ REMOVE STUDENT")
        print(" [3] ➤ MODIFY DETAILS")
        print(" [4] ➤ VIEW RECORDS")
        print(" [0] ➤ EXIT PROGRAM")
        print("\n" + "=" * 50)
        print("=" * 50)

        ch = int(input("Enter your choice: "))
        if ch == 1:
            add()
        elif ch == 2:
            remove()
        elif ch == 3:
            modify()
        elif ch == 4:
            view()
        elif ch == 0:
            print("Exiting program...")
            break
        else:
            print("Invalid choice")

    mycon.close()
else:
    print("Connection failed")