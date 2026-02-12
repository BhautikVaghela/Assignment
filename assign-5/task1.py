# Create a dictionary of student marks
students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 95,
    "Eve": 88
}

# Ask user to input a student's name
name = input("Enter the student's name: ")

# Retrieve and display marks or show error message
if name in students:
    print(f"{name}'s marks: {students[name]}")
else:
    print("Student not found.")
