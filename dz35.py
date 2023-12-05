class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.gender}, {self.age} years old'


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{super().__str__()}, Record Book: {self.record_book}'


class GroupFullError(Exception):
    pass


class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) < 10:
            self.group.add(student)
        else:
            raise GroupFullError("Група вже має максимальну кількість студентів (10)")

    def delete_student(self, last_name):
        student_to_delete = self.find_student(last_name)
        if student_to_delete:
            self.group.remove(student_to_delete)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Number: {self.number}\n{all_students}'


# Тестування
st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')

try:
    for _ in range(11):
        gr.add_student(st1)
except GroupFullError as e:
    print(e)  # Група вже має максимальну кількість студентів (10)

gr.add_student(st2)
print(gr)
