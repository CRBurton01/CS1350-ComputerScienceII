# CS1350 - Computer Science II
# Cody Burton
# 1/13/2026
# CS1350-Week1-Lab.py

# Lecture 1
# Unit 1.1 - Dictionary Fundamentals
my_info = {"name" : "Cody", "age" : 19, "major" : "Cybersecurity"}

menu = {"burger" : 5.99, "chicken" : 6.99, "fries" : 2.99, "soda" : 1.99}

# Unit 1.2 - Accessing Dictionary Elements
print(my_info["name"])
print(menu.get("fries"))
# print(menu["salad"]) - CAUSES KEY ERROR, CRASH!!!
print(menu.get("salad")) # Returns None, does not crash
print(my_info.get("hobby", "No hobby listed")) # Returns default value, does not crash

pet = {"name": "Buddy", "type": "dog", "age": 3}

print(pet["name"], pet["age"])

print(pet.get("color", "unknown"))

# Unit 1.3 - Modifying Dictionaries

# Adding new key-value pairs
grades = {"Alice": 85}
grades["Bob"] = 92
print(grades)

# Modifying existing key-value pairs
grades["Alice"] = 88
print(grades)

# Removing key-value pairs
del grades["Bob"]
print(grades)

# Using pop() to remove a key-value pair and get its value
grades = {"Alice": 85, "Bob": 92}
removed = grades.pop("Bob")
print(removed)  # Output: 92

inventory = {}
inventory["apples"] = 10
inventory["oranges"] = 5
inventory["bananas"] = 7
print(inventory)

scores = {"Team A": 45, "Team B": 38}
scores["Team B"] = 52
scores["Team C"] = 41
removed_teams = scores.pop("Team A")
print(f"Removed Team A with score {removed_teams}")
print(scores)

# End of Lecture 1

# Lecture 2
# Unit 2.1 - How Dictionaries Work

# Hashing
print(hash("Alice")) # -1234567890123456789 (varies by session)
print(hash(42)) # 42 (integers hash to themselves)
print(hash((1, 2))) # 3713081631934410656 (tuples are hashable)

# Dictionary keys must be IMMUTABLE and HASHABLE
# Valid keys: strings, numbers, tuples (with immutable elements), booleans, None, frozensets
# Invalid keys: lists, dictionaries, sets

# Mistakes

# Using a list as a key
# data = {[1, 2]: "bad"}  TypeError: unhashable type: 'list'
# Fix: Convert to tuple
data = {(1, 2): "good"} # Works!

# Duplicate keys, the last value will overwrite previous ones
grades = {"Alice": 85, "Alice": 92}
print(grades) # {"Alice": 92}
print(len(grades)) # 1, not 2!

# Forgetting quotes for string keys
name = "Bob"
data = {name: 100} # Uses variable value: {"Bob": 100}
data = {"name": 100} # Uses literal string: {"name": 100}
# These are different!

# Mutable default arguments
# WRONG - the same dict is shared across calls!
#def add_item(item, container={}):
#    container[item] = True
#    return container

# CORRECT
def add_item(item, container=None):
    if container is None:
        container = {}
        container[item] = True
        return container
    
# Exercises

#Which of these are valid dictionary keys? Write "valid" or "invalid" and explain why:
#a)"student_name"  (valid, reason: strings are immutable and hashable)
#b) [1, 2, 3]  (invalid, reason: lists are mutable and not hashable)
#c) 100  (valid, reason: integers are immutable and hashable)
#d) ("x", "y")  (valid, reason: tuples are immutable and hashable)
#e) {"a": 1}  (invalid, reason: dictionaries are mutable and not hashable)
#f) frozenset({1,2})  (valid, reason: frozensets are immutable and hashable)

#This code will cause an error. Why? How can you fix it?
# locations = {[40.7, -74.0]: "New York", [34.0, -118.2]: "Los Angeles"}

# The keys are lists, which are mutable and not hashable. To fix it, we can convert the lists to tuples:
# locations = {(40.7, -74.0): "New York", (34.0, -118.2): "Los Angeles"}

# What will this code print?
data = {"a": 1, "b": 2, "a": 3, "b": 4}
print(data) # Output: {'a': 3, 'b': 4} - the last value for each duplicate key overwrites the previous ones
print(len(data)) # Output: 2 - there are only 2 unique keys ('a' and 'b'), not 4.

#What is the hash value of your name? What about the number 100?
print(hash("Cody")) # Output will vary each time progam is run
print(hash(100)) # Output: 100 - integers hash to themselves

# Unit 2.2 - keys() and values() Methods

#keys()
grades = {"Alice": 85, "Bob": 92, "Carol": 78}
print(grades.keys()) # dict_keys(['Alice', 'Bob', 'Carol'])
print(type(grades.keys())) # <class 'dict_keys'>

# Common uses for keys()
# Check if a key exists: if "Alice" in grades.keys(): (or just in grades)
# Loop through all keys
# Convert to list: list(grades.keys())

#values()
grades = {"Alice": 85, "Bob": 92, "Carol": 78}
print(grades.values()) # dict_values([85, 92, 78])

# Common uses for values()
# Find the highest/lowest: max(grades.values()), min(grades.values())
# Calculate sum/average: sum(grades.values()) / len(grades)
# Check if a value exists: if 85 in grades.values():

# keys(), values(), and items() return view objects, not lists!
# Views are are dynamic, dont support indexing, and are very memory efficient

# Additional Methods
d = {"a": 1, "b": 2}

# Check if key exists (O(1) - fast!)
# "a" in d # True
# "c" in d # False

# Get number of items
len(d) # 2

# Remove all items
d.clear() # d is now {}

# Get with default, add if missing
d.setdefault("c", 3) # Returns 3, adds {"c": 3} to dict

# Update multiple values at once
d.update({"x": 10, "y": 20}) # Adds/updates multiple keys

# Create a shallow copy
d2 = d.copy()

# Exercises
temps = {"Monday": 72, "Tuesday": 75, "Wednesday": 68}
#1) Print all the days in the dictionary using keys().
print(temps.keys())
#2) Print all the temperatures using values().
print(temps.values())
#3) Print how many days are in the dictionary.
print(len(temps))

# 1) Find and print the highest and lowest temperatures from temps.
print(max(temps.values()))
print(min(temps.values()))
# 2) Check if "Friday" is in the dictionary using the in operator. Print an appropriate message.
if "Friday" in temps:
    print("Friday is in the dictionary.")
else:
    print("Friday is not in the dictionary.")
# 3) Use setdefault() to add "Thursday" with a value of 70, but only if it doesn't exist.
temps.setdefault("Thursday", 70)
# 4) Demonstrate that views are dynamic: create a keys view, add a new day, show the view updated.
keys_view = temps.keys()
temps["Friday"] = 75
print(keys_view)

# Unit 2.3 - The items() Method

# items() returns a view of (key, value) pairs as tuples
grades = {"Alice": 85, "Bob": 92}
print(grades.items())
# dict_items([('Alice', 85), ('Bob', 92)])

# Tuple Unpacking
# Without unpacking (awkward)
pair = ('Alice', 85)
name = pair[0] # 'Alice'
grade = pair[1] # 85

# With unpacking (clean!)
name, grade = ('Alice', 85)
print(name) # 'Alice'
print(grade) # 85

# unpacking works on any iterable of the correct length!!

# Iterating over items() is not slower than iterating over keys() or values()!!
# Exercises 
colors = {"apple": "red", "banana": "yellow", "grape": "purple"}
# 1) Use a for loop to print each fruit and its color
for fruit, color in colors.items():
    print(f"The {fruit} is {color}")
# 2) Without running the code, predict what list(colors.items()) returns.
#It returns a list of tuples. [('apple', 'red'), ('banana', 'yellow'), ('grape', 'purple')]

# 1) Given prices = {"coffee": 4.50, "tea": 3.00, "juice": 5.25}, write a loop using items() that prints each item with 10% tax added
prices = {"coffee": 4.50, "tea": 3.00, "juice": 5.25}
for item, price in prices.items():
    tax = price * 0.10
    print(f"{item}: ${price} + ${tax} tax = ${price + tax}")
# 2) Count how many items in prices cost more than $4.00 using iteration.
count = 0
for price in prices.values():
    if price > 4.00:
        count += 1
print(f"Number of items costing more than $4.00: {count}")
# 3) Use tuple unpacking to swap two variables x = 10 and y = 20 in one line.
x, y = 10, 20
x, y = y, x
# 4) Given a list [1, 2, 3, 4, 5], use extended unpacking to get the first element, last element, andmiddle elements separately.
numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers
print(f"First: {first}, Middle: {middle}, Last: {last}")

# End of Lecture 2 - End of Lab