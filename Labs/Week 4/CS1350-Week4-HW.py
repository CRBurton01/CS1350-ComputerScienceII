# CS1350 - Computer Science II
# Cody Burton
# 1/27/2026
# CS1350-Week3-HW.py

# Program Imports
import numpy as np

#Problem 1: Array Creation and Basic Operations
print("=" * 10 + " Problem 1 " + "=" * 10)

#Part A: Create Arrays (10 points)
# Create the following arrays and print each with a label:
# 1. zeros_arr: A 1D array of 8 zeros
zeros_arr = np.zeros(8)
print("zeros_arr:", zeros_arr)

# 2. ones_matrix: A 3×4 matrix of ones
ones_matrix = np.ones((3, 4))
print("ones_matrix:", ones_matrix)

# 3. range_arr: Numbers from 10 to 50 (inclusive) with step 5: [10, 15, 20, ..., 50]
range_arr = np.arange(10, 51, 5)
print("range_arr:", range_arr)

# 4. linear_arr: 9 evenly spaced numbers from 0 to 2 (inclusive)
linear_arr = np.linspace(0, 2, 9)
print("linear_arr:", linear_arr)
print()

#Part B: Basic Operations
a = np.array([2, 4, 6, 8, 10])
b = np.array([1, 2, 3, 4, 5])

print(a+b)
print(a*b)
print(a**2)
print(a/b)
print(np.sum(a))
print(np.mean(b))
print()

#Problem 2: Array Attributes and Statistics
print("=" * 10 + " Problem 2 " + "=" * 10)

#Part A: Array Attributes
#Create a 4×5 matrix containing integers 1-20, then print:
matrix = np.arange(1, 21).reshape(4, 5)
print(matrix)
print("Shape:", matrix.shape)
print("Number of dimensions:", matrix.ndim)
print("Total elements:", matrix.size)
print("Data type:", matrix.dtype)
print("Bytes used:", matrix.nbytes)
print()

#Part B: Statistics
print("Mean:", np.mean(matrix))
print("Standard Deviation:", np.std(matrix))
print("Minimum:", np.min(matrix))
print("Maximum:", np.max(matrix))
print("Sum of each row:", np.sum(matrix, axis=1))
print("Mean of each column:", np.mean(matrix, axis=0))
print("Index of max element:", np.unravel_index(np.argmax(matrix), matrix.shape))
print()

#Problem 3: Indexing and Boolean Selection
print("=" * 10 + " Problem 3 " + "=" * 10)

# Student scores: 6 students, 4 exams
scores = np.array([
[85, 90, 78, 92], # Alice
[70, 65, 72, 68], # Bob
[95, 98, 94, 97], # Carol
[60, 55, 58, 62], # Dave
[88, 85, 90, 87], # Eve
[75, 80, 77, 82] # Frank
])
students = ['Alice', 'Bob', 'Carol', 'Dave', 'Eve', 'Frank']
exams = ['Exam1', 'Exam2', 'Exam3', 'Exam4']

#Part A: Indexing
print("Carol Exam2 score:", scores[2, 1])
print("Alice scores:", scores[0])
print("All Exam3 scores:", scores[:, 2])
print("Bob and Carol Exam1 and Exam2 scores:", scores[1:3, 0:2])
print()

#Part B: Boolean Selection
# 1. Create a boolean mask for all scores >= 90
high_scores_mask = scores >= 90
print("Boolean mask for scores >= 90:\n", high_scores_mask)
# 2. Print all scores that are >= 90
print("All scores >= 90:\n", scores[high_scores_mask])
# 3. Count how many scores are >= 90
print("Number of scores >= 90:", np.sum(high_scores_mask))
# 4. Find which students have an average score >= 85 (print their names)
print("Students with average score >= 85:")
average_scores = np.mean(scores, axis=1)
for i, avg in enumerate(average_scores):
    if avg >= 85:
        print(students[i])

# 5. Replace all failing scores (< 60) with 60 (minimum passing grade). Print the modified array.
scores[scores < 60] = 60
print("Modified scores with failing grades replaced:\n", scores)
print()

# Problem 4: Reshaping and Broadcasting
print("=" * 10 + " Problem 4 " + "=" * 10)

#Part A: Reshaping
arr_1d = np.arange(1, 25)
print("Original 1D array:", arr_1d)
arr_2d = arr_1d.reshape(4, 6)
print("Reshaped to 4x6:\n", arr_2d)
arr_3d = arr_1d.reshape(2, 3, 4)
print("Reshaped to 2x3x4:\n", arr_3d)
flattened = arr_3d.flatten()
print("Flattened back to 1D:", flattened)
print()

#Part B: Broadcasting
# Rows: products (Apple, Banana, Orange)
# Columns: stores (Store1, Store2, Store3, Store4)
prices = np.array([
[1.20, 1.50, 1.30, 1.40], # Apple
[0.50, 0.60, 0.55, 0.45], # Banana
[0.80, 0.90, 0.85, 0.75] # Orange
])

#Use broadcasting to:
#1. Apply a 10% discount to ALL prices (multiply by 0.9)
discounted_prices = prices * 0.9
print("Prices after 10% discount:\n", discounted_prices)
#2. Add a $0.10 delivery fee to each store (add [0.10, 0.10, 0.10, 0.10] to each row)
delivery_fee = np.array([0.10, 0.10, 0.10, 0.10])
prices_with_delivery = prices + delivery_fee
print("Prices with delivery fee:\n", prices_with_delivery)
#3. The stores have different tax rates: [0.08, 0.06, 0.07, 0.05]. Calculate the final price with tax for each product in each store.
tax_rates = np.array([0.08, 0.06, 0.07, 0.05])
prices_with_tax = prices_with_delivery * (1 + tax_rates)
print("Prices with tax:\n", prices_with_tax)
#4. Normalize prices by subtracting each product's mean price (center the data by row)
mean_prices = np.mean(prices, axis=1).reshape(-1, 1)
normalized_prices = prices - mean_prices
print("Normalized prices (centered by product):\n", normalized_prices)
print()

print("=" * 10 + " End of Homework 3 " + "=" * 10)