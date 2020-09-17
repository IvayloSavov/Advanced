def input_to_list(count_students):
    students = []

    for _ in range(count_students):
        student = input()
        students.append(student)

    return students


def students_marks(students):
    dict_students = {}

    for s in students:
        (name, mark) = s.split(" ")
        if name not in dict_students:
            dict_students[name] = []
        dict_students[name].append(float(mark))

    return dict_students


def avg(grades):
    return sum(grades) / len(grades)


def print_result(dict_students):

    for student, marks in dict_students.items():
        avg_grade = avg(marks)
        marks_str = [f"{mark:.2f}" for mark in marks]
        marks_str = " ".join(marks_str)
        print(f"{student} -> {marks_str} (avg: {avg_grade:.2f})")


n = int(input())
test_input = input_to_list(n)
print_result(students_marks(test_input))