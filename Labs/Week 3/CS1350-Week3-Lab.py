# CS1350 - Computer Science II
# Cody Burton
# 1/27/2026
# CS1350-Week3-Lab.py

# Lecture 1
# Unit 1: Sets Theory and Sets in Python

# Creating sets
from unittest import result


colors = {"red", "green", "blue"}
print(f"Colors: {colors}")
print(f"Type: {type(colors)}")

# Duplicates removed
numbers = {1, 2, 2, 3, 3, 3}
print(f"Numbers (dupes removed): {numbers}")

# From list - great for deduplication!
grades = [85, 90, 85, 78, 90, 85]
unique_grades = set(grades)
print(f"Unique grades: {unique_grades}")

# Empty set vs empty dict
empty_set = set()
empty_dict = {}
print(f"Empty set type: {type(empty_set)}")
print(f"Empty dict type: {type(empty_dict)}")

# Membership testing (fast!)
big_set = set(range(100000))
print(f"99999 in big_set: {99999 in big_set}")
print(f"100001 in big_set: {100001 in big_set}")

# Practice Exercises
vowels = {'a', 'e', 'i', 'o', 'u'}
print(f"Vowels: {vowels}")

my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
my_set = set(my_list)
print(f"My set (from list): {my_set}")

# Whats wrong with this code? empty = {}
empty = set() # This creates an empty set, the other creates an empty dictionary
print(f"Empty set type corrected: {type(empty)}")

text = "mississippi"
unique_chars = set(text)
print(f"Unique characters in 'mississippi': {unique_chars}")

emails = ["a@b.com", "c@d.com", "a@b.com", "e@f.com", "c@d.com"]
unique_emails = list(set(emails))
print(f"Unique emails: {unique_emails}")
print(f"Number of unique emails: {len(unique_emails)}")

# Why does this fail? s = {[1, 2], [3, 4]}
# Sets require their elements to be hashable (immutable). Lists are mutable and thus unhashable.
s = {(1, 2), (3, 4)} # Using tuples instead of lists
print(f"Set with tuples: {s}")

# Unit 2: Set Operations
# | Union - Both sets combined
# & Intersection - Common elements
# - Difference - In the first set but not the second
# ^ Symmetric Difference - In either set but not both

a = {1, 2, 3}
b = {3, 4, 5}

# Union
full_set = a | b # or a.union(b)
print(f"Union (a | b): {full_set}")

cs_students = {"Alice", "Bob", "Carol"}
math_students = {"Bob", "Dave", "Eve"}
all_students = cs_students | math_students
# {"Alice", "Bob", "Carol", "Dave", "Eve"}

# Intersection
print(a&b) # or a.intersection(b)
common_students = cs_students & math_students
print(f"Intersection (a & b): {common_students}")

# Difference
print(a - b) # or a.difference(b)
cs_only_students = cs_students - math_students
print(f"Difference (a - b): {cs_only_students}")

# Symmetric Difference
print(a ^ b) # or a.symmetric_difference(b)
either_but_not_both = cs_students ^ math_students
print(f"Symmetric Difference (a ^ b): {either_but_not_both}")

# Combining operations
a = {1, 2, 3}
b = {2, 3, 4}
c = {3, 4, 5}

# Elements in all three sets
all_three = a & b & c # {3}
# Elements in any set
any_set = a | b | c # {1, 2, 3, 4, 5}
# In a but not in b or c
a_only = a - b - c # {1}

a = {1, 2}
b = {1, 2, 3, 4}

# Is a a subset of b? (all a's elements in b)
print(a <= b) # True
print(a.issubset(b)) # True

# Is b a superset of a? (b contains all of a)
print(b >= a) # True
print(b.issuperset(a)) # True

# Proper subset (subset but not equal)
print(a < b) # True (a is proper subset)
print(a < a) # False (a equals a)

# Practice Exercises
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

unique = a | b
print(f"Union of a and b: {unique}")

both = a & b
print(f"Intersection of a and b: {both}")

only_a = a - b
print(f"Difference of a and b (a - b): {only_a}")

morning_shift = {"Alice", "Bob", "Carol"}
evening_shift = {"Carol", "Dave", "Eve"}
weekend_shift = {"Alice", "Eve", "Frank"}

works_all_shifts = morning_shift & evening_shift & weekend_shift
print(f"Works all shifts: {works_all_shifts}")
works_any_shift = morning_shift | evening_shift | weekend_shift
print(f"Works any shift: {works_any_shift}")
works_morning_only = morning_shift - evening_shift - weekend_shift
print(f"Works morning shift only: {works_morning_only}")
works_one_shift = (morning_shift ^ evening_shift) ^ weekend_shift
print(f"Works exactly one shift: {works_one_shift}")

# Unit 3: Set Methods, Comprehensions, & Patterns
colors = {"red", "blue"}
colors.add("green")
print(f"Colors after add: {colors}")
colors.update(["yellow", "purple"])
print(f"Colors after update: {colors}")

colors.remove("blue") # KeyError if not found
print(f"Colors after remove: {colors}")

colors.discard("pink") # No error if not found
print(f"Colors after discard: {colors}")

popped_color = colors.pop() # Removes and returns an arbitrary element
print(f"Popped color: {popped_color}")

colors.clear()
print(f"Colors after clear: {colors}")

# copy() returns a shallow copy of the set

# Update Operations
a = {1, 2, 3}
b = {3, 4, 5}

# In-place union
a |= b  # a = a | b
print(f"a after |= b: {a}") # {1, 2, 3, 4, 5}

# In-place intersection
a = {1, 2, 3}
a &= {2, 3, 4} # Same as a.intersection_update({2, 3, 4})
print(a) # {2, 3}

# In-place difference
a = {1, 2, 3}
a -= {2} # Same as a.difference_update({2})
print(a) # {1, 3}

# In-place symmetric difference
a = {1, 2, 3}
a ^= {2, 3, 4} # Same as a.symmetric_difference_update(...)
print(a) # {1, 4}

# Set Comparisons
a = {1, 2}
b = {1, 2, 3}
c = {1, 2}

# Equality
print(a == c) # True

# Subset
print(a <= b) # True
print(a.issubset(b)) # True

# Superset
print(b >= a) # True
print(b.issuperset(a)) # True

# Disjoint
print(a.isdisjoint({4, 5})) # True
print(a.isdisjoint(b)) # False

# Set Comprehensions
# Basic syntax
# {expression for item in iterable}

# Example: Square numbers
squares = {x**2 for x in range(1, 6)}
print(squares) # {1, 4, 9, 16, 25}

# With condition
evens = {x for x in range(10) if x % 2 == 0}
print(evens) # {0, 2, 4, 6, 8}

# From string
letters = {char.lower() for char in "Hello World" if char.isalpha()}
print(letters) # {'h', 'e', 'l', 'o', 'w', 'r', 'd'}

# Common Set Patterns
# Remove duplicates, preserve order
def unique_ordered(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print(unique_ordered(data)) # [3, 1, 4, 5, 9, 2, 6]

# Find missing items
required = {"name", "email", "password"}
provided = {"name", "email"}
missing = required - provided
print(f"Missing fields: {missing}") # {'password'}

# Validation check
valid_codes = {"A", "B", "C", "D", "E"}
user_input = ["A", "X", "B", "Z", "C"]
invalid = {code for code in user_input if code not in valid_codes}
print(f"Invalid codes: {invalid}") # {'X', 'Z'}

# Practice Exercises
numbers = {1, 2, 3}
numbers.add(4)
numbers.discard(1)
print(f"Numbers after add and discard: {numbers}")

evens = {x for x in range(1, 21) if x % 2 == 0}
print(f"Evens from 1 to 20: {evens}")

# evens.remove(19) - Raises KeyError
evens.discard(19)  # No error

my_list = [4, 5, 2, 4, 8, 5, 2, 1, 9, 4]
unique_ordered_list = unique_ordered(my_list)

sentence = "To be or not to be that is the question"
unique_words = {word.lower() for word in sentence.split()}
print(f"Unique words in sentence: {unique_words}")

expected = set(range(1, 11))
actual = {1, 2, 4, 5, 7, 8, 10}
# Find missing numbers
missing_numbers = expected - actual

# End of Lecture 1

