# Python Basics Assignment

You are developing a simple Student Management System. Complete the following tasks:

## Task 1: Student Data Management
Create a dictionary of students where:
- Keys are student IDs (strings)
- Values are dictionaries containing:
  - name (string)
  - age (int)
  - grades (list of 3 subjects)

Example structure:
```python
students = {
    "ST101": {
        "name": "John Smith",
        "age": 20,
        "grades": [85, 90, 88]
    }
}
```

## Task 2: Grade Processing
Create a function that:
1. Takes a student ID as input
2. Returns:
   - Average grade
   - Highest grade
   - Lowest grade
   - "Pass" if average ≥ 60, else "Fail"

## Task 3: Student Report
Create a function that:
1. Loops through all students
2. Prints a formatted report showing:
   - Student ID
   - Name
   - Age
   - Grade status (Pass/Fail)

## Sample Data
Use this data to test your code:
```python
students = {
    "ST101": {"name": "John Smith", "age": 20, "grades": [85, 90, 88]},
    "ST102": {"name": "Emma Davis", "age": 19, "grades": [55, 60, 58]},
    "ST103": {"name": "Alex Johnson", "age": 21, "grades": [95, 92, 96]}
}
```

## Bonus Task
Add functionality to:
1. Add new students
2. Update student grades
3. Remove students
4. Sort students by average grade


Good luck! 🚀


# Submission Instructions

## Create a new GitHub repository named `machine-vision`

1. Your repository should include:

   - Folder named `assignment-1-solution`
        - `README.md`
        - notebook with your solution

**Note:** Make sure your repository is public so it can be accessed.
