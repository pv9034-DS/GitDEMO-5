# Python Practice Programs

This repository contains two simple Python programs for practicing **dictionaries** and **lists**.

---

## 📘 Program 1: Student Marks Dictionary

### Problem Statement:
1. Create a dictionary where student names are keys and their marks are values.  
2. Ask the user to input a student's name.  
3. Retrieve and display the corresponding marks.  
4. If the student’s name is not found, display an appropriate message.  

### Code:
```python
students = {
    "Amit": 85,
    "Pooja": 92,
    "Rahul": 76,
    "Sneha": 89,
    "Arjun": 95
}

name = input("Enter the student's name: ")

if name in students:
    print(f"{name}'s marks: {students[name]}")
else:
    print("Student not found.")

### output
Enter the student's name: Rahul
Rahul's marks are: 76


## 📘 Program 2: List Operations (Original, Extracted, and Reversed)

###Problem Statement:

Create a list of numbers from 1 to 10.
Extract the first five elements from the list.
Reverse these extracted elements.
Print the original list, the extracted list, and the reversed list.

### Code:
numbers = list(range(1, 11))

first_five = numbers[:5]
reversed_list = first_five[::-1]

print("Original list:", numbers)
print("Extracted list:", first_five)
print("Reversed list:", reversed_list)

### output:
Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Extracted list: [1, 2, 3, 4, 5]
Reversed list: [5, 4, 3, 2, 1]

