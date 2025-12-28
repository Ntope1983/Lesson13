# This function allows you to create a student record with an arbitrary number of grades (*args)
# and additional information passed as keyword arguments (**kwargs), such as the student's name
# and the list of lessons they are taking.
#
# It calculates the student's average grade and compares their lessons with all previously
# added students to find and display any common lessons. Finally, it stores the student
# in the global 'students' list for future comparisons.
#
# Key concepts demonstrated:
# - Using *args to accept multiple grades
# - Using **kwargs to accept flexible additional information
# - Calculating averages
# - Comparing sets to find common elements
# - Maintaining a list of student records
def create_student(*args, **kwargs):
    # Calculate average grade
    total = 0
    for grade in args:
        total += grade
    average_grade = total / len(args)

    current_name = kwargs["name"]
    current_lessons = set(kwargs["lessons"])

    print(f"The student {current_name} has average grade {average_grade}")

    # Compare with existing students
    for student in students:
        other_name = student[1]["name"]
        other_lessons = set(student[1]["lessons"])

        common_lessons = current_lessons & other_lessons
        if common_lessons:
            print(f"  Shares lessons with {other_name}: {common_lessons}")

    # Add student AFTER comparisons
    students.append((args, kwargs))


students = []

create_student(
    5, 6, 7, 8.5, 9,
    name="Polydoras",
    lessons=["Computer Science", "Discrete Mathematics", "Algorithms",
             "Artificial Intelligence", "Cybersecurity"]
)

create_student(
    5.5, 6, 5, 8, 10,
    name="Papadopoulos",
    lessons=["Programming", "Discrete Mathematics", "Algorithms",
             "Math/Ethics", "Databases"]
)

create_student(
    5, 3, 5, 9.4, 10,
    name="Vlasic",
    lessons=["Linear Algebra", "English for IT Support", "Algorithms",
             "Logic Design Laboratory", "Databases"]
)
