def add_student():
name = input("Student name: ")
marks = input("Marks separated by spaces: ")
students[name] = [int(m) for m in marks.split()]
print(f"Added {name}.")

def calculate_grade(average):
if average >= 85:
return "A"
elif average >= 70:
return "B"
elif average >= 55:
return "C"
elif average >= 40:
return "D"
return "F"
def show_grades():
if not students:
print("No students yet.")
return
for name, marks in students.items():
average = sum(marks) / len(marks)
print(f"{name}: average {average:.1f}, grade 
{calculate_grade(average)}")
def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "0":
            print("Goodbye!")
            break

        elif choice == "1":
            name = input("Enter student name: ")
            if name in students:
                print("Student already exists.")
            else:
                students[name] = []
                print("Student added successfully.")

        elif choice == "2":
            if not students:
                print("No students found.")
            else:
                for name, marks in students.items():
                    print(f"{name}: {marks}")

        elif choice == "3":
            name = input("Enter student name: ")
            if name in students:
                try:
                    mark = float(input("Enter mark: "))
                    students[name].append(mark)
                    print("Mark added successfully.")
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("Student not found.")

        elif choice == "4":
            name = input("Enter student name: ")
            if name in students:
                marks = students[name]
                if marks:
                    average = sum(marks) / len(marks)
                    print(f"Average marks: {average:.2f}")
                else:
                    print("No marks available.")
            else:
                print("Student not found.")

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
