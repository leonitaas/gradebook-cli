import unittest
from gradebook.service import (
    add_student,
    add_course,
    enroll,
    add_grade,
    compute_average
)


class TestService(unittest.TestCase):

    def test_add_student(self):
        sid = add_student("Test User")
        self.assertTrue(sid > 0)

    def test_add_grade_and_average(self):
        sid = add_student("Student A")
        add_course("CS50", "Intro CS")
        enroll(sid, "CS50")
        add_grade(sid, "CS50", 100)

        avg = compute_average(sid, "CS50")
        self.assertEqual(avg, 100)

    def test_invalid_grade(self):
        with self.assertRaises(ValueError):
            add_grade(1, "CS50", 200)


if __name__ == "__main__":
    unittest.main()