import pytest
from student import Student, StudentManagementSystem

studentOb = StudentManagementSystem()


class TestStudentManagementSystem():

    def test_accept_student_valid_input(self):
        # Arrange
        roll_no = '1'
        name = 'John'
        marks = '80'

        # Act
        result = studentOb.accept_student(roll_no, name, marks)

        # Assert
        assert result == "Student added successfully"
        assert len(studentOb.students) == 1
        assert studentOb.students[0].roll_no == 1
        assert studentOb.students[0].name == 'John'
        assert studentOb.students[0].marks == 80

    def test_accept_student_valid_input_unique_roll(self):

        studentOb.students.append(Student(1, 'John', 80))

        # Arrange
        name = "John"
        roll_no = "1"
        marks = "80"

        # Act
        result = studentOb.accept_student(roll_no, name, marks)

        # Assert
        assert result == "Please Enter Unique Roll"

    def test_accept_student_invalid_input(self):

        studentOb.clearList()

        # Arrange
        roll_no = 'A'
        name = '123'
        marks = 'X'

        # Act
        result = studentOb.accept_student(roll_no, name, marks)

        # Assert
        assert result == "Invalid Roll Number"
        assert len(studentOb.students) == 0

    def test_search_student_valid_input_found(self):
        # Arrange
        studentOb.students.append(Student(1, 'John', 80))
        roll_no = '1'

        # Act
        result = studentOb.search_student(roll_no)

        # Assert
        assert result == "John"

    def test_display_student_empty_list(self):
        studentOb.clearList()

        # Act
        result = studentOb.display_students()

        # Assert
        assert result == "No students added yet"

    def test_search_student_valid_input_not_found(self):
        # Arrange
        studentOb.students.append(Student(1, 'John', 80))
        roll_no = '2'

        # Act
        result = studentOb.search_student(roll_no)

        # Assert
        assert result == "Student not found"

    def test_search_student_invalid_input(self):
        # Arrange
        roll_no = 'A'

        # Act
        result = studentOb.search_student(roll_no)

        # Assert
        assert result == "Invalid Roll Number"

    def test_delete_student_valid_input_found(self):
        studentOb.clearList()
        # Arrange
        studentOb.students.append(Student(1, 'John', 80))
        roll_no = '1'

        # Act
        result = studentOb.delete_student(roll_no)

        # Assert
        assert result == "Student deleted successfully"
        assert len(studentOb.students) == 0

    def test_delete_student_valid_input_not_found(self):
        studentOb.clearList()
        # Arrange
        studentOb.students.append(Student(1, 'John', 80))
        roll_no = '2'

        # Act
        result = studentOb.delete_student(roll_no)

        # Assert
        assert result == "Student not found"
        assert len(studentOb.students) == 1

    def test_delete_student_invalid_input(self):
        studentOb.clearList()
        # Arrange
        roll_no = 'A'

        # Act
        result = studentOb.delete_student(roll_no)

        # Assert
        assert result == "Invalid input for roll number"
        assert len(studentOb.students) == 0

    def test_update_student_valid_input(self):
        studentOb.clearList()

        # Arrange
        studentOb.students.append(Student(1, 'Sid', 80))
        roll_no = '1'
        name = "John"
        marks = "50"

        # Act
        result = studentOb.update_student(roll_no, name, marks)

        # Assert
        assert result == "Student updated successfully"
        assert len(studentOb.students) == 1
        assert studentOb.students[0].roll_no == 1
        assert studentOb.students[0].name == 'John'
        assert studentOb.students[0].marks == 50

    def test_update_student_invalid_input(self):
        studentOb.clearList()

        # Arrange
        studentOb.students.append(Student(1, 'Sid', 80))
        roll_no = 'A'
        name = "John"
        marks = "50"

        # Act
        result = studentOb.update_student(roll_no, name, marks)

        # Assert
        assert result == "Invalid Roll Number"

    def test_update_student_not_found(self):
        studentOb.clearList()

        # Arrange
        studentOb.students.append(Student(1, 'Sid', 80))
        roll_no = '2'
        name = "John"
        marks = "50"

        # Act
        result = studentOb.update_student(roll_no, name, marks)

        # Assert
        assert result == "Student not found"
