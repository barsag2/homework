class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lect(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in self.courses_in_progress and
                       course in lecturer.courses_attached):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        all_grades = []
        for grades_list in self.grades.values():
            all_grades.extend(grades_list)
        if all_grades:
            return round(sum(all_grades) / len(all_grades), 1) if all_grades else 0
        return 0

    def __lt__(self, other):
        if not isinstance(other, Student):
            return False
        return self.average_grade() < other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return self.average_grade() == other.average_grade()

    def __str__(self):
        avg = self.average_grade()
        in_progress = ', '.join(self.courses_in_progress)
        finished = ', '.join(self.finished_courses)
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {avg}\n'
                f'Курсы в процессе изучения: {in_progress}\n'
                f'Завершенные курсы: {finished}')


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        all_grades = []
        for grades_list in self.grades.values():
            all_grades.extend(grades_list)
        if all_grades:
            return round(sum(all_grades) / len(all_grades), 1) if all_grades else 0
        return 0

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return False
        return self.average_grade() < other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return False
        return self.average_grade() == other.average_grade()

    def __str__(self):
        avg = self.average_grade()
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg}'

def average_homework_grade_by_course(students, course_name):
    all_grades = []
    for s in students:
        if course_name in s.grades:
            all_grades.extend(s.grades[course_name])
    return round(sum(all_grades) / len(all_grades), 1) if all_grades else 0.0

def average_lecture_grade_by_course(lecturers, course_name):
    all_grades = []
    for l in lecturers:
        if course_name in l.grades:
            all_grades.extend(l.grades[course_name])
    return round(sum(all_grades) / len(all_grades), 1) if all_grades else 0.0




some_lecturer_1 = Lecturer('Иван', 'Иванов')
some_lecturer_2 = Lecturer('Петр', 'Петров')

some_reviewer_1 = Reviewer('Василий', 'Васильев')
some_reviewer_2 = Reviewer('Александр', 'Александров')

some_student_1 = Student('Андрей', 'Андреев', 'М')
some_student_2 = Student('Евгений', 'Евгеньев', 'М')

some_student_1.courses_in_progress += ['Java', 'Git']
some_student_2.courses_in_progress += ['Python', 'Git']

some_student_1.finished_courses += ['Введение в програмирование']
some_student_2.finished_courses += ['Введение в програмирование']

some_lecturer_1.courses_attached += ['Java', 'Git']
some_lecturer_2.courses_attached += ['Python', 'Git']

some_reviewer_1.courses_attached += ['Python', 'Git']
some_reviewer_2.courses_attached += ['Python', 'Java']

students = [some_student_1, some_student_2]
lecturers = [some_lecturer_1, some_lecturer_2]

some_student_1.rate_lect(some_lecturer_1, 'Java', 9)
some_student_1.rate_lect(some_lecturer_2, 'Git', 7)
some_student_1.rate_lect(some_lecturer_1, 'Python', 10)
some_student_1.rate_lect(some_lecturer_2, 'Git', 8)
some_student_2.rate_lect(some_lecturer_1, 'Python', 10)
some_student_2.rate_lect(some_lecturer_2, 'Java', 8)
some_student_2.rate_lect(some_lecturer_1, 'Java', 7)
some_student_2.rate_lect(some_lecturer_2, 'Java', 7)

some_reviewer_1.rate_hw(some_student_1, 'Java', 9)
some_reviewer_1.rate_hw(some_student_1, 'Git', 8)
some_reviewer_1.rate_hw(some_student_1, 'Java', 5)
some_reviewer_1.rate_hw(some_student_1, 'Python', 8)
some_reviewer_2.rate_hw(some_student_2, 'Git', 9)
some_reviewer_2.rate_hw(some_student_2, 'Python', 10)
some_reviewer_2.rate_hw(some_student_2, 'Git', 7)
some_reviewer_2.rate_hw(some_student_2, 'Python', 10)

avg_python_st = average_homework_grade_by_course(students, 'Python')
avg_git_st = average_homework_grade_by_course(students, 'Git')
avg_java_st = average_homework_grade_by_course(students, 'Java')

avg_python_lt = average_lecture_grade_by_course(lecturers, 'Python')
avg_git_lt = average_lecture_grade_by_course(lecturers, 'Git')
avg_java_lt = average_lecture_grade_by_course(lecturers, 'Java')

print(some_lecturer_2)
print()
print(some_lecturer_1)
print()
print(some_student_1)
print()
print(some_student_2)
print()
print(some_reviewer_1)
print()
print(some_reviewer_2)
print()
print(some_student_1 < some_student_2)
print('Средняя оценка студентов по Java:', avg_java_st)
print('Средняя оценка студентов по Python:', avg_python_st)
print('Средняя оценка лекторов курса по Git:', avg_git_lt)
print('Средняя оценка лекторов курса по Java:', avg_java_lt)

