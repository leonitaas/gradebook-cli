class Student:
    def __init__(self, id, name):
        if not name or not name.strip():
            raise ValueError("Student name cannot be empty")

        self.id = id
        self.name = name.strip()

    def __str__(self):
        return f"Student(id={self.id}, name='{self.name}')"


class Course:
    def __init__(self, code, title):
        if not code or not code.strip():
            raise ValueError("Course code cannot be empty")

        if not title or not title.strip():
            raise ValueError("Course title cannot be empty")

        self.code = code.strip()
        self.title = title.strip()

    def __str__(self):
        return f"Course(code='{self.code}', title='{self.title}')"


class Enrollment:
    def __init__(self, student_id, course_code, grades=None):
        self.student_id = student_id
        self.course_code = course_code
        self.grades = grades if grades else []

        for g in self.grades:
            if not isinstance(g, (int, float)) or not (0 <= g <= 100):
                raise ValueError("Grades must be numbers between 0 and 100")

    def __str__(self):
        return (
            f"Enrollment(student_id={self.student_id}, "
            f"course_code='{self.course_code}', grades={self.grades})"
        )