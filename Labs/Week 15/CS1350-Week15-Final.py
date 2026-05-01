# CS1350 - Computer Science II
# Cody Burton
# 5/1/2026
# CS1350-Week15-Final.py

# Problem 1: Gradebook Summary
grades = {
    "alice": {"CS1350": [85, 92, 78], "MATH201": [90, 88]},
    "bob": {"CS1350": [72, 75, 80], "PHYS100": [65, 70]},
    "carol": {"CS1350": [95, 98, 92], "MATH201": [85, 90]},
}

def gradebook_summary(grades):
    summary = {}
    # student_averages: dict mapping student name to their average grade across all courses
    student_averages = {}
    # course_averages: dict mapping course name to average grade across all students
    course_averages = {}
    # top_per_course: dict mapping course name to (student_name, average_grade) of the top student in that course
    top_per_course = {}
    for student, courses in grades.items():
        total = 0
        count = 0
        for course, grades_list in courses.items():
            avg = sum(grades_list) / len(grades_list)
            total += sum(grades_list)
            count += len(grades_list)
            # Update course averages
            if course not in course_averages:
                course_averages[course] = []
            course_averages[course].append(avg)
            # Update top student per course
            if course not in top_per_course or avg > top_per_course[course][1]:
                top_per_course[course] = (student, avg)
        student_averages[student] = total / count if count > 0 else 0
    # Populate the summary dictionary
    summary["student_averages"] = student_averages
    summary["course_averages"] = course_averages
    summary["top_per_course"] = top_per_course
    return summary

print(gradebook_summary(grades))

# Problem 2: Candidate Skill Matcher

candidates = {
    "alice": {'python', 'sql', 'git', 'docker'},
    "bob": {'java', 'sql', 'git'},
    "carol": {'python', 'sql', 'git', 'docker', 'kubernetes'},
    "dave": {'java', 'c++'},
    "eve": {'python', 'sql'}
}
required = {'python', 'sql', 'git'}

def skill_analysis(candidates, required):
    analysis = {}
    # fully_qualified: sorted list of candidates who have all required skills
    fully_qualified = [candidate for candidate, skills in candidates.items() if required <= skills]
    analysis["fully_qualified"] = sorted(fully_qualified)
    # best_match: candidate with the most required skills (if tie, only return first candidate alphabetically)
    best_match = []
    max_skills = 0
    for candidate, skills in candidates.items():
        count = len(required & skills)
        if count > max_skills:
            max_skills = count
            best_match = [candidate]
        elif count == max_skills:
            best_match.append(candidate)
    analysis["best_match"] = sorted(best_match)[0] if best_match else None
    # unique_skills: dict mapping candidates to sorted list of skills they possess that no other candidate has. Omit candidates with no unique skills.
    unique_skills = {}
    for candidate, skills in candidates.items():
        unique = skills - set().union(*(candidates[c] for c in candidates if c != candidate))
        if unique:
            unique_skills[candidate] = sorted(unique)
    analysis["unique_skills"] = unique_skills
    return analysis

print(skill_analysis(candidates, required))