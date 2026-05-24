#Wap to read details of student for result preparation. Incorporate exception handling such as ValueError,IndexError,ZeroDivisionError,etc

students = []

def calculate_result(marks):
    """Calculate percentage and grade, handling ZeroDivisionError."""
    try:
        total = sum(marks)
        percentage = (total / len(marks))  # Potential ZeroDivisionError if empty list
        if percentage >= 75:
            grade = "Distinction"
        elif percentage >= 60:
            grade = "First Division"
        elif percentage >= 50:
            grade = "Second Division"
        elif percentage >= 40:
            grade = "Pass"
        else:
            grade = "Fail"
        return total, percentage, grade
    except ZeroDivisionError:
        print("Error: No marks provided for calculation.")
        return 0, 0.0, "Invalid"

while True:
    try:
        name = input("Enter student name: ").strip()
        if not name:
            print("Name cannot be empty.")
            continue
        
        roll_no = input("Enter roll number: ").strip()
        marks_input = input("Enter marks in 3 subjects (space-separated): ").strip().split()
        
        # Handle IndexError for insufficient marks
        if len(marks_input) != 3:
            print("Error: Exactly 3 marks required.")
            continue
        
        marks = []
        for mark_str in marks_input:
            mark = float(mark_str)  # Potential ValueError
            if 0 <= mark <= 100:
                marks.append(mark)
            else:
                raise ValueError("Marks must be between 0 and 100.")
        
        total, percentage, grade = calculate_result(marks)
        student = {
            'name': name,
            'roll_no': roll_no,
            'marks': marks,
            'total': total,
            'percentage': round(percentage, 2),
            'grade': grade
        }
        students.append(student)
        print(f"Added {name} successfully.\n")
        
    except ValueError as ve:
        print(f"Input Error: {ve}. Please enter valid numbers.\n")
    except IndexError:
        print("Error: Invalid list access during processing.\n")
    except KeyboardInterrupt:
        print("\nInput stopped by user.")
        break
    except Exception as e:
        print(f"Unexpected error: {e}\n")

# Display results table
if students:
    print("\n## Student Results Summary")
    print("| Name | Roll No | Marks | Total | % | Grade |")
    print("|------|---------|-------|-------|---|-------|")
    for i, student in enumerate(students, 1):
        marks_str = ', '.join(map(str, student['marks']))
        print(f"| {student['name']} | {student['roll_no']} | {marks_str} | {student['total']} | {student['percentage']} | {student['grade']} |")
else:
    print("No student data recorded.")
