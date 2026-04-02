from .storage import load_data, save_data

def _find_student(data, student_id):
    return next((s for s in data["students"] if s["id"] == student_id), None)


def _find_course(data, course_code):
    return next((c for c in data["courses"] if c["code"] == course_code), None)


def add_student(name):
    data = load_data()
    new_id = max([s["id"] for s in data["students"]], default=0) + 1

    data["students"].append({"id": new_id, "name": name})
    save_data(data)
    return new_id


def add_course(code, title):
    data = load_data()

    if _find_course(data, code):
        raise ValueError("Course already exists")

    data["courses"].append({"code": code, "title": title})
    save_data(data)


def enroll(student_id, course_code):
    data = load_data()

    if not _find_student(data, student_id):
        raise ValueError("Student not found")

    if not _find_course(data, course_code):
        raise ValueError("Course not found")

    exists = any(
        e["student_id"] == student_id and e["course_code"] == course_code
        for e in data["enrollments"]
    )

    if exists:
        raise ValueError("Already enrolled")

    data["enrollments"].append({
        "student_id": student_id,
        "course_code": course_code,
        "grades": []
    })

    save_data(data)


def add_grade(student_id, course_code, grade):
    if not (0 <= grade <= 100):
        raise ValueError("Invalid grade")

    data = load_data()

    for e in data["enrollments"]:
        if e["student_id"] == student_id and e["course_code"] == course_code:
            e["grades"].append(grade)
            save_data(data)
            return

    raise ValueError("Enrollment not found")


def list_students(sort="name"):
    data = load_data()
    return sorted(data["students"], key=lambda x: x[sort])


def list_courses(sort="code"):
    data = load_data()
    return sorted(data["courses"], key=lambda x: x[sort])


def list_enrollments():
    data = load_data()
    return data["enrollments"]


def compute_average(student_id, course_code):
    data = load_data()

    for e in data["enrollments"]:
        if e["student_id"] == student_id and e["course_code"] == course_code:
            return sum(e["grades"]) / len(e["grades"]) if e["grades"] else 0

    raise ValueError("Enrollment not found")


def compute_gpa(student_id):
    data = load_data()

    avgs = [
        sum(e["grades"]) / len(e["grades"])
        for e in data["enrollments"]
        if e["student_id"] == student_id and e["grades"]
    ]

    return sum(avgs) / len(avgs) if avgs else 0