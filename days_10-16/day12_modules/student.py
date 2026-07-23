# -----------------------------------------------------------
# student.py
# Student class with encapsulated name and marks.
# Part of Day 12: Modules and Packages
# -----------------------------------------------------------


class Student:
    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks

    def get_name(self):
        """Return the student's name."""
        return self.__name

    def get_marks(self):
        """Return the student's current marks."""
        return self.__marks

    def set_marks(self, marks):
        """Update marks, but only if within the valid 0-100 range."""
        if marks < 0 or marks > 100:
            print("Invalid Marks")
        else:
            self.__marks = marks


# -----------------------------------------------------------
# Test code — only runs when this file is executed directly,
# not when it's imported by another file (like main.py)
# -----------------------------------------------------------
if __name__ == "__main__":
    student1 = Student("Krishna Dwivedi", 94)
    print(student1.get_name())
    print(student1.get_marks())
    student1.set_marks(90)
    print(student1.get_marks())
    