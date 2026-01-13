# CS1350 - Computer Science II
# Cody Burton
# 1/13/2026
# CS1350-Week1-Lab.py

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

