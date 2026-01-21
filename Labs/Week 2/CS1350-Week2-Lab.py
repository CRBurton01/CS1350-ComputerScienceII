# CS1350 - Computer Science II
# Cody Burton
# 1/21/2026
# CS1350-Week2-Lab.py

# Lecture 1
# Unit 3.1 - Iterating Through Dictionaries
grades = {"Alice": 85, "Bob": 92, "Carol": 78}
for student in grades: # Iterates over Keys
    print(f"{student}")

for score in grades.values(): # Iterates over Values
    print(f"{score}")

# Great for calculations
total = sum(grades.values())
average = total / len(grades)

for name, score in grades.items(): # Iterates over Key-Value Pairs
    print(f"{name} has a score of {score}")
    
# Why items() is better than key + lookup:
# Less efficient - extra lookup each time
for name in grades:
    score = grades[name] # Hash lookup every iteration

# More effecient - direct access
for name, score in grades.items(): # No extra lookup
    pass

# Practice Exercises
inventory = {"apples": 50, "bananas": 30, "oranges": 25}
for fruit in inventory:
    print(f"{fruit}")

total_items = 0
for quantity in inventory.values():
    total_items += quantity

for fruit, quantity in inventory.items():
    print(f"There are {quantity} {fruit} in stock.")
    
prices = {"laptop": 999, "phone": 699, "tablet": 449, "watch": 299}
for key in sorted(prices):
    print(f"{key}")

for key in sorted(prices, key=prices.get, reverse=True): # type: ignore
    print(f"{key}: ${prices[key]}")

# Unit 3.2 - Advanced Iteration and Nested Dictionaries
grades = {"Alice": 85, "Bob": 92, "Carol": 78}

for i, (name, score) in enumerate(grades.items(), start=1):
    print(f"{i}. {name}: {score}")
    
names = ["Alice", "Bob", "Carol"]
scores = [85, 92, 78]

grades = {}
for name, score in zip(names, scores):
    grades[name] = score
print(grades)

# Dont modify a dictionary while iterating over it!
# for name, score in grades.items():
#   if score < 70:
#       del grades[name]  # This will cause a RuntimeError

# Correct way - iterate over a copy of the keys
for name, score in list(grades.items()):
    if grades[name] < 70:
        del grades[name] # Safe!
        
 # Nested Dictionaries
students = {
    "Alice": {"grade": 85, "major": "CS", "year": 2},
    "Bob": {"grade": 92, "major": "Math", "year": 3}
}
print(students["Alice"]["major"]) # "CS"
print(students["Bob"]["grade"])  # 92

# Safe nested access
grade = students.get("Charlie", {}).get("grade", "N/A")
print(grade)  # "N/A"

for name, info in students.items():
    print(f"\n{name}:")
    for field, value in info.items():
        print(f"  {field}: {value}")

# Practice Exercises
products = {
    "laptop": {"price": 999, "stock": 15},
    "phone": {"price": 699, "stock": 50}
}
for product, details in products.items():
    print(f"{product}:")
    for key, value in details.items():
        print(f"  {key}: {value}")
        
countries = ["USA", "Canada", "Mexico"]
capitals = ["Washington", "Ottawa", "Mexico City"]
country_info = {}
for country, capital in zip(countries, capitals):
    country_info[country] = {"capital": capital}
print(country_info)

products["tablet"] = {"price": 449, "stock": 30}
for product, details in list(products.items()):
    if details["stock"] < 20:
        del products[product]
print(products)

# Unit 3.3 - Dictionary Patterns and Transformations
# Basic syntax
# {key_expression: value_expression for item in iterable (if condition)}
# Example: Square numbers
squares = {x: x**2 for x in range(1, 6)}
print(squares) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

prices = {"apple": 1.00, "banana": 0.50}
doubled = {item: price * 2 for item, price in prices.items()}
# {"apple": 2.00, "banana": 1.00}

data = {"a1": 10, "a2": 20, "b1": 30}
a_only = {k: v for k, v in data.items() if k.startswith("a")}
# {"a1": 10, "a2": 20}

grades = {"Alice": 85, "Bob": 72}

# Add curve
curved = {n: min(g + 5, 100) for n, g in grades.items()}

# Convert to letters
def to_letter(s):
    if s >= 90: return "A"
    if s >= 80: return "B"
    if s >= 70: return "C"
    return "F"

letters = {n: to_letter(g) for n, g in grades.items()}

original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
# {1: "a", 2: "b", 3: "c"}

words = ["apple", "banana", "apple","cherry", "apple"]
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
# {"apple": 3, "banana": 1, "cherry": 1}

students = [("Alice", "CS"), ("Bob", "Math"), ("Carol", "CS")]
by_major = {}
for name, major in students:
    if major not in by_major:
        by_major[major] = []
    by_major[major].append(name)
# {"CS": ["Alice", "Carol"], "Math": ["Bob"]}
# Practice Exercises
cubes = {x: x**3 for x in range(1, 6)}
print(cubes)

temps = {"Mon": 72, "Tue": 68, "Wed": 75}
tempsC = {day: (temp - 32) * 5/9 for day, temp in temps.items()}

scores = {"Alice": 88, "Bob": 65, "Carol": 92, "Dave": 71, "Eve": 58}
passing = {name: score for name, score in scores.items() if score >= 70}
print(passing)
letter_grades = {name: ("A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F") for name, score in scores.items()}
print(letter_grades)
student_ids = {"Alice": 101, "Bob": 102}
st_id_inverted = {id_: name for name, id_ in student_ids.items()}
print(st_id_inverted)

# End of Lecture 1