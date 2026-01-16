# CS1350 - Computer Science II
# Cody Burton
# 1/16/2026
# CS1350-Week1-HW.py

# Problem 1 - Contact Manager
# Part A - Create and Populate
print("Problem 1 - Contact Manager")
print("\nPart A - Create and Populate")
# - Create an empty dictionary called contacts
contacts = {}
# - Add the following contacts (name as key, phone number as string value):
contacts["Mom"] = "555-1234"
contacts["Dad"] = "555-5678"
contacts["Best Friend"] = "555-8888"
contacts["Pizza Place"] = "555-9999"
contacts["Work"] = "555-0000"
# - Print the contact list
print(f"Contact List: {contacts}")
    
# Part B - Access and Modify
print("\nPart B - Access and Modify")
# - Print Mom's phone number using bracket notation
print(f"Mom's number: {contacts['Mom']}")
# - Dad got a new number! Update it to "555-4321"
contacts["Dad"] = "555-4321"
# - Add a new contact: "Dentist": "555-2222"
contacts["Dentist"] = "555-2222"
# - Use get() to look up "Grandma" - if not found, print "Contact not found"
grandma_number = contacts.get("Grandma", "Contact not found")
print(f"Grandma's number: {grandma_number}")
# - Print the updated contact list
print(f"Updated Contact List: {contacts}")

# Part C - Delete and Analyze
print("\nPart C - Delete and Analyze")
# - You no longer need Pizza Place. Remove it using del
del contacts["Pizza Place"]
# - You're switching jobs. Use pop() to remove "Work" and save the old number
work_number = contacts.pop("Work")
# - Print the removed work number
print(f"Removed Work number: {work_number}")
# - Print how many contacts remain (use len())
print(f"Number of contacts remaining: {len(contacts)}")
# - Print all contact names using keys()
print(f"All contact names: {list(contacts.keys())}")
# - Print all phone numbers using values()
print(f"All contact numbers: {list(contacts.values())}")

# Problem 2 - Grade Book Analyzer
# Part A - Basic Statistics
print("\n" + "="*50)
print("Problem 2 - Grade Book Analyzer")
print("\nPart A - Basic Statistics")
grades = {
"Alice": 87,
"Bob": 65,
"Carol": 92,
"Dave": 78,
"Eve": 55,
"Frank": 88,
"Grace": 71,
"Henry": 95,
"Ivy": 60,
"Jack": 83
}
# - Print all student names using keys()
print(f"Student Names:{grades.keys()}")
# - Print all grades using values()
print(f"Grades:{grades.values()}")
# - Calculate and print:
    # Total number of students
print(f"Total number of students: {len(grades)}")
    # Sum of all grades
print(f"Sum of all grades: {sum(grades.values())}")
    # Class average (formatted to 2 decimal places)
print(f"Class average: {sum(grades.values()) / len(grades):.2f}")
    # Highest grade (use max())
print(f"Highest grade: {max(grades.values())}")
    # Lowest grade (use min())
print(f"Lowest grade: {min(grades.values())}")

# Part B - Iteration and Analysis
print("\nPart B - Iteration and Analysis")
# Using items() and for loops...
# - Print each student with their grade and letter grade:
for name, grade in grades.items():
    if grade >= 90:
        letter = "A"
    elif grade >= 80:
        letter = "B"
    elif grade >= 70:
        letter = "C"
    elif grade >= 60:
        letter = "D"
    else:
        letter = "F"
    print(f"{name}: {grade} ({letter})")
# - Count and print
    # How many students passed (grade >= 60)
pass_count = 0
for grade in grades.values():
    if grade >= 60:
        pass_count += 1
print(f"Number of students who passed: {pass_count}")
    # Number of students who failed (below 60)
fail_count = 0
for grade in grades.values():
    if grade < 60:
        fail_count += 1
print(f"Number of students who failed: {fail_count}")
    # Number of A grades, B grades, C grades, D grades, F grades
a_count = sum(1 for grade in grades.values() if grade >= 90)
b_count = sum(1 for grade in grades.values() if 80 <= grade < 90)
c_count = sum(1 for grade in grades.values() if 70 <= grade < 80)
d_count = sum(1 for grade in grades.values() if 60 <= grade < 70)
f_count = sum(1 for grade in grades.values() if grade < 60)

print(f"Number of A grades: {a_count}")
print(f"Number of B grades: {b_count}")
print(f"Number of C grades: {c_count}")
print(f"Number of D grades: {d_count}")
print(f"Number of F grades: {f_count}")

# Part C: Find Specific Students
print("\nPart C - Find Specific Students")
# Using loops with items()...
# - Find and print the name of the student with the HIGHEST grade
highest_student = max(grades, key=grades.get) # type: ignore
print(f"Student with highest grade: {highest_student} ({grades[highest_student]})")

# - Find and print the name of the student with the LOWEST grade
lowest_student = min(grades, key=grades.get) # type: ignore
print(f"Student with lowest grade: {lowest_student} ({grades[lowest_student]})")

# - Find and print all students scoring above the class average
above_average_students = [name for name, grade in grades.items() if grade > sum(grades.values()) / len(grades)]
print(f"Students scoring above the class average: {above_average_students}")

# End of Homework