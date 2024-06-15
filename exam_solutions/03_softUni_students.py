def softuni_students(*args, **kwargs):
    student_course = {}
    invalid_students = set()
    for every_arg in args:
        for key, value in kwargs.items():
            if every_arg[0] == key:
                student_course[every_arg[1]] = value
            if every_arg[0] not in kwargs:
                invalid_students.add(every_arg[1])

    sorted_student_course = dict(sorted(student_course.items()))
    result = []
    for username, course in sorted_student_course.items():
        result.append(f"*** A student with the username {username} has successfully finished the course {course}!")
    if invalid_students:
        result.append(f"!!! Invalid course students: {', '.join(sorted(invalid_students))}")
    return '\n'.join(result)


print(softuni_students(    ('id_22', 'Programmingkitten'),    ('id_11', 'MitkoTheDark'),
                           ('id_321', 'Bobosa253'),    ('id_08', 'KrasimirAtanasov'),    ('id_32', 'DaniBG'),
                           id_321='HTML & CSS',    id_22='Machine Learning',    id_08='JS Advanced',))