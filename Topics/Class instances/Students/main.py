class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the student_id here
        self.student_id = name[0] + last_name + str(birth_year)


first_name = input()
surname = input()
byear = input()
student = Student(first_name, surname, byear)

print(student.student_id)
