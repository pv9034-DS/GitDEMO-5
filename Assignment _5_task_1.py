# Step 1: Create a dictionary with student names and their marks
students = {
    "Amit": 85,
    "Pooja": 92,
    "Rahul": 76,
    "Sneha": 89,
    "Arjun": 95
}

# Step 2: Ask user to input a student's name
name = input("Enter the student's name: ")

# Step 3 & 4: Retrieve and display marks (or message if not found)
if name in students:
    print(f"{name}'s marks: {students[name]}")
else:
    print("Student not found.")
