import argparse
from gradebook import service
from gradebook.utils import parse_grade


def main():
    parser = argparse.ArgumentParser(description="Gradebook CLI")
    subparsers = parser.add_subparsers(dest="command")

    s = subparsers.add_parser("add-student")
    s.add_argument("--name", required=True)

    c = subparsers.add_parser("add-course")
    c.add_argument("--code", required=True)
    c.add_argument("--title", required=True)

    e = subparsers.add_parser("enroll")
    e.add_argument("--student-id", type=int, required=True)
    e.add_argument("--course", required=True)

    g = subparsers.add_parser("add-grade")
    g.add_argument("--student-id", type=int, required=True)
    g.add_argument("--course", required=True)
    g.add_argument("--grade", required=True)

    l = subparsers.add_parser("list")
    l.add_argument("type", choices=["students", "courses", "enrollments"])
    l.add_argument("--sort") 

    a = subparsers.add_parser("avg")
    a.add_argument("--student-id", type=int, required=True)
    a.add_argument("--course", required=True)

    gp = subparsers.add_parser("gpa")
    gp.add_argument("--student-id", type=int, required=True)

    args = parser.parse_args()

    try:
        if args.command == "add-student":
            sid = service.add_student(args.name)
            print(f"Student added with ID: {sid}")

        elif args.command == "add-course":
            service.add_course(args.code, args.title)
            print("Course added")

        elif args.command == "enroll":
            service.enroll(args.student_id, args.course)
            print("Enrolled successfully")

        elif args.command == "add-grade":
            grade = parse_grade(args.grade)
            service.add_grade(args.student_id, args.course, grade)
            print("Grade added")

        elif args.command == "list":
            if args.type == "students":
                sort_key = args.sort or "name"
                for s in service.list_students(sort_key):
                    print(f"{s['id']} - {s['name']}")
            
            elif args.type == "courses":
                sort_key = args.sort or "title"
                for c in service.list_courses(sort_key):
                    print(f"{c['code']} - {c['title']}")
            else:
                for e in service.list_enrollments():
                    print(
                        f"Student {e['student_id']} | "
                        f"Course {e['course_code']} | "
                        f"Grades: {e['grades']}"
                    )

        elif args.command == "avg":
            avg = service.compute_average(args.student_id, args.course)
            print(f"Average: {avg:.2f}")

        elif args.command == "gpa":
            gpa = service.compute_gpa(args.student_id)
            print(f"GPA: {gpa:.2f}")

        else:
            parser.print_help()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()