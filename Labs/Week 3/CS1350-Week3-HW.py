# CS1350 - Computer Science II
# Cody Burton
# 1/27/2026
# CS1350-Week3-HW.py

# Problem 1: Movie Rating Analyzer
ratings = {
 "Alice": {"Inception": 5, "Titanic": 3, "Avatar": 4, "Jaws": 2},
 "Bob": {"Inception": 4, "The Matrix": 5, "Avatar": 5, "Jaws": 3},
 "Carol": {"Titanic": 5, "The Matrix": 4, "Avatar": 3, "Interstellar": 5},
 "Dave": {"Inception": 3, "Titanic": 4, "The Matrix": 5, "Jaws": 4},
 "Eve": {"Inception": 5, "Avatar": 4, "Interstellar": 4, "Jaws": 1}
}

#Part A: User Statistics
print("=" * 10 + " Problem 1 " + "=" * 10)
print("Part A - User Statistics:")
for user, movies in ratings.items():
    count = len(movies)
    average = sum(movies.values()) / count
    favorite_movie = max(movies, key=movies.get) # type: ignore
    print(f"{user}: {count} movies, average rating: {average:.2f}, favorite: {favorite_movie} ({movies[favorite_movie]})")
print()

#Part B: Movie Statistics
print("Part B - Movie Statistics:")
movie_stats = {}
recommendations = []
for movies in ratings.values():
    for movie, score in movies.items():
        if movie not in movie_stats:
            movie_stats[movie] = []
        movie_stats[movie].append(score)
for movie, scores in movie_stats.items():
    count = len(scores)
    average = sum(scores) / count
    if average >= 4:
        recommendations.append(movie)
    print(f"{movie}: {average:.2f} avg ({count} ratings)")
print()
print(movie_stats)

#Part C: Recommendations
print("Part C - Recommendations:")
print("Recommendations for Alice:")
for movie in movie_stats:
    if movie not in ratings["Alice"] and movie in recommendations:
        print(f"{movie}") 
print()

# Problem 2: Sales Data Transformer
sales_records = [
 {"product": "Laptop", "category": "Electronics", "price": 999, "quantity": 5,"region": "North"},
 {"product": "Mouse", "category": "Electronics", "price": 25, "quantity": 50,"region": "North"},
 {"product": "Desk", "category": "Furniture", "price": 350, "quantity": 8,"region": "South"},
 {"product": "Chair", "category": "Furniture", "price": 150, "quantity": 20,"region": "South"},
 {"product": "Laptop", "category": "Electronics", "price": 999, "quantity": 3,"region": "South"},
 {"product": "Keyboard", "category": "Electronics", "price": 75, "quantity":30, "region": "North"},
 {"product": "Desk", "category": "Furniture", "price": 350, "quantity": 5,"region": "North"},
 {"product": "Monitor", "category": "Electronics", "price": 300, "quantity": 12, "region": "South"},
]

#Part A: Dictionary Comprehensions
print("=" * 10 + " Problem 2 " + "=" * 10)
print("Part A - User Statistics:")
product_prices = {record["product"]: record["price"] for record in sales_records}
print("Product Prices:")
print(product_prices)
print()

expensive_products = {product: price for product, price in product_prices.items() if price > 100}
print("Expensive Products (> $100):")
print(expensive_products)
print()

price_category = {record["product"]: ("premium" if record["price"] >= 300 else "standard") for record in sales_records}
print("Price Categories:")
print(price_category)
print()


#Part B: Aggregation Patterns
print("Part B - Aggregation Patterns:")
total_by_category = {} # Total revenue by category
for record in sales_records:
    category = record["category"]
    revenue = record["price"] * record["quantity"]
    total_by_category[category] = total_by_category.get(category, 0) + revenue
print("Total Revenue by Category:")
print(total_by_category)
print()

total_by_region = {} # Total revenue by region
for record in sales_records:
    region = record["region"]
    revenue = record["price"] * record["quantity"]
    total_by_region[region] = total_by_region.get(region, 0) + revenue
print("Total Revenue by Region:")
print(total_by_region)
print()

quantity_by_product = {} # Total quantity sold by product
for record in sales_records:
    product = record["product"]
    quantity = record["quantity"]
    quantity_by_product[product] = quantity_by_product.get(product, 0) + quantity
print("Total Quantity Sold by Product:")
print(quantity_by_product)
print()

#Problem 3: Course Regristration System

# Students and their registered courses
registrations = {
 "Alice": {"CS101", "CS201", "MATH101"},
 "Bob": {"CS101", "MATH101", "PHYS101"},
 "Carol": {"CS201", "CS301", "MATH201"},
 "Dave": {"CS101", "CS201", "MATH101", "PHYS101"},
 "Eve": {"CS301", "MATH201", "MATH301"}
}
# Course prerequisites (must have taken these BEFORE registering)
prerequisites = {
 "CS101": set(), # No prerequisites
 "CS201": {"CS101"}, # Must have CS101
 "CS301": {"CS201"}, # Must have CS201
 "MATH101": set(), # No prerequisites
 "MATH201": {"MATH101"}, # Must have MATH101
 "MATH301": {"MATH201"}, # Must have MATH201
 "PHYS101": {"MATH101"} # Must have MATH101
}
# Course capacities and current enrollment
capacity = {"CS101": 30, "CS201": 25, "CS301": 20, "MATH101": 35, "MATH201": 25,
"MATH301": 20, "PHYS101": 30}

# Part A: Set Operations
print("=" * 10 + " Problem 3 " + "=" * 10)
print("Part A - Set Operations:")
all_courses = set()
for courses in registrations.values():
    all_courses |= courses
print(f"All unique courses being taken: {all_courses}")

common_courses = set.intersection(*(courses for courses in registrations.values()))
print(f"Courses taken by all students: {common_courses}")

only_alice_courses = registrations["Alice"] - set.union(*(courses for student, courses in registrations.items() if student != "Alice"))
print(f"Courses only Alice is taking: {only_alice_courses}")

students_in_CS = {student for student, courses in registrations.items() if any(course.startswith("CS") for course in courses)}
print(f"Students in any CS course: {students_in_CS}")
print()

# Part B: Prerequisite Validation
print("Part B - Prerequisite Validation:")
for student, courses in registrations.items():
    for course in courses:
        prereqs = prerequisites.get(course, set())
        if not prereqs.issubset(courses):
            missing = prereqs - courses
            print(f"{student} is missing prerequisites {missing} for course {course}")
print()
# Part C: Enrollment Analysis
print("Part C - Enrollment Analysis:")
overloaded_students = {student for student, courses in registrations.items() if len(courses) > 3}
print(f"Students enrolled in 4+ courses: {overloaded_students}")
# Set of all math courses taken by students
math_courses_taken = {course for courses in registrations.values() for course in courses if course.startswith("MATH")}
print(f"Math courses taken by students: {math_courses_taken}")
# Students with exact same courses
course_sets = {}
for student, courses in registrations.items():
    course_tuple = tuple(sorted(courses))
    if course_tuple not in course_sets:
        course_sets[course_tuple] = []
    course_sets[course_tuple].append(student)
same_course_students = {tuple_: studs for tuple_, studs in course_sets.items() if len(studs) > 1}
print(f"Students with identical course registrations: {same_course_students}")
print()
# Enrollment count per course
enrollment_count = {}
for courses in registrations.values():
    for course in courses:
        enrollment_count[course] = enrollment_count.get(course, 0) + 1
print(f"Enrollment count per course: {enrollment_count}")
print()
print(f"Under-enrolled courses (<3 students): {[course for course, count in enrollment_count.items() if count < 3]}")
print()

print("=" * 10 + " End of Homework " + "=" * 10)
# End of CS1350-Week3-HW.py