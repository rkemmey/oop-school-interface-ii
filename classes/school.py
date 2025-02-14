from classes.staff import Staff
from classes.student import Student

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.objects()
        self.students = Student.objects()

    def list_students(self):
        counter = 1
        for s in self.students:
            print(f'{counter}. {s.name} {s.school_id}')
            counter+=1

    def find_student_by_id(self, id):
        for s in self.students:
            if str(s.school_id) == str(id):
                return s
            
    def add_student(self, data):
        try:
            new = Student(**data)
            self.students.append(new)
            print(new)
        except Exception as e:
            print(e)

    def delete_student(self):
        student = self.find_student_by_id()
        for s in self.students:
            if str(s.school_id) == student:
                self.students.remove(s)
                print('removed')
                return None