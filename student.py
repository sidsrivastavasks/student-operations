class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"{self.roll_no}\t{self.name}\t{self.marks}"


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def accept_student(self, roll_no, name, marks):

        # Basic validations
        if not roll_no.isdigit():
            return "Invalid Roll Number"
        if not name.isalpha():
            return "Invalid input for name"
        if not marks.isdigit():
            return "Invalid input for marks"

        for student in self.students:
            if student.roll_no == int(roll_no):
                return "Please Enter Unique Roll"
        self.students.append(Student(int(roll_no), name, int(marks)))
        return "Student added successfully"

    def display_students(self):
        if not self.students:
            return "No students added yet"

        for student in self.students:
            return student

    def search_student(self, roll_no):

        # Basic validation
        if not roll_no.isdigit():
            return "Invalid Roll Number"

        for student in self.students:
            if student.roll_no == int(roll_no):
                return student.name

        return "Student not found"

    def delete_student(self, roll_no):

        # Basic validation
        if not roll_no.isdigit():
            return "Invalid input for roll number"

        for i, student in enumerate(self.students):
            if student.roll_no == int(roll_no):
                del self.students[i]
                return "Student deleted successfully"

        return "Student not found"

    def update_student(self, roll_no, name, marks):

        # Basic validation
        if not roll_no.isdigit():
            return "Invalid Roll Number"

        for student in self.students:
            if student.roll_no == int(roll_no):

                # Basic validations
                if not name.isalpha():
                    return "Invalid input for name"

                if not marks.isdigit():
                    return "Invalid input for marks"

                student.name = name
                student.marks = int(marks)
                return "Student updated successfully"

        return "Student not found"

    def clearList(self):
        self.students = []
