class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.rating_average = float()

    def add_courses(self, courses_name):
        self.finished_course.append(courses_name)

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in \
                lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        grades_count = 0
        courses_in_progress_string = ','.join(self.courses_in_progress)
        finished_courses_string = ','.join(self.finished_courses)
        for k in self.grades:
            grades_count += len(self.grades[k])
        self.rating_average = sum(map(sum, self.grades.values())) / grades_count
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашнее задание: {self.rating_average}\n' \
              f'Курсы в процессе обучения: {courses_in_progress_string}\n' \
              f'Завершенные курсы: {finished_courses_string}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Некорректное сравнение')
            return
        return self.rating_average < other.rating_average


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.rating_average = float()
        self.grades = {}

    def __str__(self):
        grades_count = 0
        for k in self.grades:
            grades_count += len(self.grades[k])
        self.rating_average = sum(map(sum, self.grades.values())) / grades_count
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.rating_average}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Некорректное сравнение')
            return
        return self.rating_average < other.rating_average


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\n Фамилия: {self.surname}'
        return res


One_lecturer = Lecturer('Albert', 'Einstein')
One_lecturer.courses_attached += ['Теоретическая физика']

Two_lecturer = Lecturer('Max', 'Planck')
Two_lecturer.courses_attached += ['Квантовая теория']

One_reviewer = Reviewer('Bertrand', 'Russell')
One_reviewer.courses_attached += ['Теоретическая физика']
One_reviewer.courses_attached += ['Квантовая теория']

Two_reviewer = Reviewer('John', 'Nash')
Two_reviewer.courses_attached += ['Теоретическая физика']
Two_reviewer.courses_attached += ['Квантовая теория']

One_student = Student('Stephen', 'Hoking', 'Man')
One_student.courses_in_progress += ['Теоретическая физика']
One_student.courses_in_progress += ['Квантовая теория']
One_student.finished_courses += ['Механика']

Two_student = Student('Roger', 'Penrose', 'Man')
Two_student.courses_in_progress += ['Квантовая теория']
Two_student.courses_in_progress += ['Теоретическая физика']
Two_student.finished_courses += ['Физика атома']

# Оценки:

One_student.rate_hw(One_lecturer, 'Теоретическая физика', 8)
One_student.rate_hw(One_lecturer, 'Теоретическая физика', 10)
One_student.rate_hw(One_lecturer, 'Теоретическая физика', 10)
One_student.rate_hw(Two_lecturer, 'Квантовая теория', 6)
One_student.rate_hw(Two_lecturer, 'Квантовая теория', 5)
One_student.rate_hw(Two_lecturer, 'Квантовая теория', 5)


Two_student.rate_hw(Two_lecturer, 'Квантовая теория', 8)
Two_student.rate_hw(Two_lecturer, 'Квантовая теория', 9)
Two_student.rate_hw(Two_lecturer, 'Квантовая теория', 9)
Two_student.rate_hw(One_lecturer, 'Теоретическая физика', 10)
Two_student.rate_hw(One_lecturer, 'Теоретическая физика', 8)
Two_student.rate_hw(One_lecturer, 'Теоретическая физика', 5)

One_reviewer.rate_hw(One_student, 'Теоретическая физика', 10)
One_reviewer.rate_hw(One_student, 'Теоретическая физика', 10)
One_reviewer.rate_hw(One_student, 'Теоретическая физика', 9)
One_reviewer.rate_hw(One_student, 'Квантовая теория', 9)
One_reviewer.rate_hw(One_student, 'Квантовая теория', 8)
One_reviewer.rate_hw(One_student, 'Квантовая теория', 5)
One_reviewer.rate_hw(Two_student, 'Теоретическая физика', 9)
One_reviewer.rate_hw(Two_student, 'Теоретическая физика', 9)


Two_reviewer.rate_hw(Two_student, 'Квантовая теория', 9)
Two_reviewer.rate_hw(Two_student, 'Квантовая теория', 10)
Two_reviewer.rate_hw(Two_student, 'Квантовая теория', 6)
Two_reviewer.rate_hw(Two_student, 'Теоретическая физика', 9)
Two_reviewer.rate_hw(Two_student, 'Теоретическая физика', 7)
Two_reviewer.rate_hw(Two_student, 'Теоретическая физика', 4)
Two_reviewer.rate_hw(One_student, 'Теоретическая физика', 4)
Two_reviewer.rate_hw(One_student, 'Теоретическая физика', 4)


# Оценка лектора:
print(f'Список лекторов:\n\n{One_lecturer}\n\n{Two_lecturer}')

# Оценка студента:
print(f'Список студентов:\n\n{One_student}\n\n{Two_student}')
print('------------------------------------------------------')

print(f'Результат сравнения студентов: '
      f'{One_student.name} {One_student.surname} < {Two_student.name} {Two_student.surname} = '
      f'{One_student > Two_student}')
print(f'Результат сравнение лекторов: '
      f'{One_lecturer.name} {One_lecturer.surname} < {Two_lecturer.name} {Two_lecturer.surname} = '
      f'{One_lecturer > Two_lecturer}')

Student_list = [One_student, Two_student]
Lecturer_list = [One_lecturer, Two_lecturer]


def student_rating(Student_list, course_name):
    sum_all = 0
    count_all = 0
    for student in Student_list:
        if student.courses_in_progress == [course_name]:
            sum_all += student.rating_average
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all


print(f"Средняя оценка для всех студентов по курсу {'Теоретическая физика'}: "
      f"{student_rating(Student_list, 'Теоретическая физика')}")
print()


def lecturer_rating(Lecturer_list, course_name):
    sum_all = 0
    count_all = 0
    for lecturer in Lecturer_list:
        if lecturer.courses_attached == [course_name]:
            sum_all += lecturer.rating_average
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all


print(f"Средняя оценка для всех лекторов по курсу {'Теоретическая физика'}: "
      f"{lecturer_rating(Lecturer_list, 'Теоретическая физика')}")
print()


























