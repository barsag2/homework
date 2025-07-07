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
                average = sum(all_grades) / len(all_grades)
                result = round(average, 1)
            else:
                result = 0
        return result



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
                average = sum(all_grades) / len(all_grades)
                result = round(average, 1)
            else:
                result = 0
        return result


    def __str__(self):
        avg = self.average_grade()
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg}'


some_lecturer = Lecturer('Some', 'Buddy')
some_reviewer = Reviewer('Some', 'Buddy')
some_student = Student('Ruoy', 'Eman', 'Ж')

some_student.courses_in_progress += ['Python', 'Git']
some_student.finished_courses += ['Введение в програмирование']
some_lecturer.courses_attached += ['Python', 'Git']
some_reviewer.courses_attached += ['Python', 'Git']

some_student.rate_lect(some_lecturer,'Python', 10)
some_student.rate_lect(some_lecturer,'Git', 9)
some_student.rate_lect(some_lecturer,'Python', 10)
some_student.rate_lect(some_lecturer,'Git', 10)
some_student.rate_lect(some_lecturer,'Python', 10)
some_student.rate_lect(some_lecturer,'Git', 10)
some_student.rate_lect(some_lecturer,'Python', 10)
some_student.rate_lect(some_lecturer,'Git', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Git', 10)
some_reviewer.rate_hw(some_student, 'Git', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Git', 9)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Git', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)

print(some_reviewer)
print()

print(some_lecturer)
print()

print(some_student)

