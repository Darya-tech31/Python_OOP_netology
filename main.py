class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def mean(self):
        grades_count = 0
        for k in self.grades:
            grades_count += len(self.grades[k])
        return sum(map(sum, self.grades.values())) / grades_count

    def __str__(self):
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашнее задание: {self.mean()}\n' \
              f'Курсы в процессе обучения: {courses_in_progress_string}\n' \
              f'Завершенные курсы: {finished_courses_string}'
        return res

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.mean() < other.mean()

    def __gt__(self, other):
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.mean() > other.mean()

    def __le__(self, other):
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.mean() <= other.mean()

    def __ge__(self, other):
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.mean() >= other.mean()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def mean(self):
        grades_count = 0
        for k in self.grades:
            grades_count += len(self.grades[k])
        return sum(map(sum, self.grades.values())) / grades_count

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {round(self.mean(), 2)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return self.mean() < other.mean()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return self.mean() > other.mean()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return self.mean() <= other.mean()

    def __ge__(self, other):
        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return self.mean() >= other.mean()


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
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


# Создаем лекторов
best_lecturer_1 = Lecturer('Ivan', 'Morin')
best_lecturer_1.courses_attached += ['Python']

best_lecturer_2 = Lecturer('Sergey', 'Rakov')
best_lecturer_2.courses_attached += ['Java']

best_lecturer_3 = Lecturer('Klim', 'Petrov')
best_lecturer_3.courses_attached += ['C#']

# Создаем проверяющих
cool_reviewer_1 = Reviewer('Darya', 'Dectereva')
cool_reviewer_1.courses_attached += ['Python']

cool_reviewer_2 = Reviewer('Kirill', 'Ivanov')
cool_reviewer_2.courses_attached += ['Java']

cool_reviewer_3 = Reviewer('Some', 'Buddy')
cool_reviewer_3.courses_attached += ['C#']

# Создаем студентов
best_student_1 = Student('Rima', 'Zhuravleva', 'M')
best_student_1.courses_in_progress += ['Python']
best_student_1.finished_courses += ['Введение в программирование']

best_student_2 = Student('Roman', 'Malikov', 'M')
best_student_2.courses_in_progress += ['Java']
best_student_2.courses_in_progress += ['C#']
best_student_2.finished_courses += ['Введение в программирование']

best_student_3 = Student('Sidor', 'Petrov', 'M')
best_student_3.courses_in_progress += ['C#']
best_student_3.courses_in_progress += ['Python']
best_student_3.finished_courses += ['Введение в программирование']

best_student_4 = Student('Anna', 'Romanova', 'W')
best_student_4.courses_in_progress += ['Java']
best_student_4.finished_courses += ['Введение в программирование']

# Выставляем оценки лекторам
best_student_1.rate_hw(best_lecturer_1, 'Python', 10)
best_student_1.rate_hw(best_lecturer_1, 'Python', 10)
best_student_1.rate_hw(best_lecturer_1, 'Python', 10)

best_student_2.rate_hw(best_lecturer_2, 'Java', 5)
best_student_2.rate_hw(best_lecturer_2, 'Java', 7)
best_student_2.rate_hw(best_lecturer_2, 'Java', 8)

best_student_2.rate_hw(best_lecturer_3, 'C#', 7)
best_student_2.rate_hw(best_lecturer_3, 'C#', 8)
best_student_2.rate_hw(best_lecturer_3, 'C#', 9)

best_student_3.rate_hw(best_lecturer_1, 'Python', 5)
best_student_3.rate_hw(best_lecturer_1, 'Python', 7)
best_student_3.rate_hw(best_lecturer_1, 'Python', 8)

best_student_3.rate_hw(best_lecturer_3, 'C#', 7)
best_student_3.rate_hw(best_lecturer_3, 'C#', 8)
best_student_3.rate_hw(best_lecturer_3, 'C#', 9)

best_student_4.rate_hw(best_lecturer_2, 'Java', 10)
best_student_4.rate_hw(best_lecturer_2, 'Java', 8)
best_student_4.rate_hw(best_lecturer_2, 'Java', 9)

# Выставляем оценки студентам за домашние задания
cool_reviewer_1.rate_hw(best_student_1, 'Python', 8)
cool_reviewer_1.rate_hw(best_student_1, 'Python', 9)
cool_reviewer_1.rate_hw(best_student_1, 'Python', 10)

cool_reviewer_2.rate_hw(best_student_2, 'Java', 8)
cool_reviewer_2.rate_hw(best_student_2, 'Java', 7)
cool_reviewer_2.rate_hw(best_student_2, 'Java', 9)

cool_reviewer_3.rate_hw(best_student_2, 'C#', 8)
cool_reviewer_3.rate_hw(best_student_2, 'C#', 7)
cool_reviewer_3.rate_hw(best_student_2, 'C#', 9)

cool_reviewer_1.rate_hw(best_student_3, 'Python', 8)
cool_reviewer_1.rate_hw(best_student_3, 'Python', 7)
cool_reviewer_1.rate_hw(best_student_3, 'Python', 9)

cool_reviewer_3.rate_hw(best_student_3, 'C#', 8)
cool_reviewer_3.rate_hw(best_student_3, 'C#', 9)
cool_reviewer_3.rate_hw(best_student_3, 'C#', 10)

cool_reviewer_2.rate_hw(best_student_4, 'Java', 8)
cool_reviewer_2.rate_hw(best_student_4, 'Java', 7)
cool_reviewer_2.rate_hw(best_student_4, 'Java', 9)

print(f'Перечень студентов:\n\n{best_student_1}\n\n{best_student_2}\n\n{best_student_3}\n\n{best_student_4}')
print()

print(f'Перечень лекторов:\n\n{best_lecturer_1}\n\n{best_lecturer_2}\n\n{best_lecturer_3}')
print()

print(f'Результат сравнения студентов (по средним оценкам за ДЗ): '
      f'{best_student_1.name} {best_student_1.surname} < {best_student_2.name} {best_student_2.surname} = {best_student_1.__lt__(best_student_2)}')
print()
print(f'Результат сравнения лекторов (по средним оценкам за лекции): '
      f'{best_lecturer_1.name} {best_lecturer_1.surname} < {best_lecturer_2.name} {best_lecturer_2.surname} = {best_lecturer_2.__lt__(best_lecturer_1)}')
print()

student_list = [best_student_1, best_student_2, best_student_3, best_student_4]
lecturer_list = [best_lecturer_1, best_lecturer_2, best_lecturer_3]


def student_rating(stud_list, course_name):
    for stud in stud_list:
        for key, values in stud.grades.items():
            if course_name == key:
                average_for_all = sum(values) / len(values)
                print(f"Студент: {stud.name} {stud.surname}\nКурс: {key}\n"
                      f"Средняя оценка для всех студентов по курсу: {round(average_for_all, 1)}\n")


def lecturer_rating(lecturs_list, course_name):
    for lect in lecturs_list:
        for key, values in lect.grades.items():
            if course_name == key:
                average_for_all = sum(values) / len(values)
                print(f"Лектор: {lect.name} {lect.surname}\nКурс: {key}\n"
                      f"Средняя оценка для всех лекторов по курсу: {round(average_for_all, 1)}\n")


student_rating(student_list, 'Python')
print()

lecturer_rating(lecturer_list, 'Python')
print()