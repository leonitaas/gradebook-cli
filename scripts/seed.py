from gradebook.storage import load_data

from gradebook.service import (
    add_student,
    add_course,
    enroll,
    add_grade
)

def seed():
    data = load_data()

    if data["courses"] or data["students"]:
        print("Data already exists, skipping seed.")
        return

    add_course("CS101", "Intro to CS")
    add_course("MATH101", "Mathematics")
    add_student("Alice")
    add_student("Bob")

    print("Seed data created successfully")
    
if __name__ == "__main__":
    seed()