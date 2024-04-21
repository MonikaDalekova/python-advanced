number_of_students = int(input())
students_grades = {}
for student in range(number_of_students):
    student_name, grade = tuple(input().split())
    grade = float(grade)
    if student_name not in students_grades:
        students_grades[student_name] = []
    students_grades[student_name].append(grade)
for name, grades in students_grades.items():
    avg = sum(grades) / len(grades)
    print(f"{name} -> {' '.join([str(f'{x:.2f}') for x in grades])} (avg: {avg:.2f})")