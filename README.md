# Gradebook CLI Application

## Overview

The Gradebook CLI Application is a command-line based system developed in Python for managing students, courses, enrollments, and grades. The project demonstrates a modular backend architecture with clear separation of concerns, data persistence, and command-line interaction.

## Features

* Add and manage students
* Add and manage courses
* Enroll students in courses
* Assign grades to enrolled students
* Compute average grade per course
* Compute GPA per student
* List students, courses, and enrollments
* Data persistence using JSON
* Input validation and error handling
* Unit testing for core functionalities

## Project Structure

```
gradebook/
│
├── gradebook/
│   ├── __init__.py
│   ├── models.py        # Data models
│   ├── service.py       # Business logic
│   ├── storage.py       # JSON data handling
│   ├── utils.py         # Helper functions
│
├── scripts/
│   └── seed.py          # Initial data setup
│
├── tests/
│   └── test_service.py  # Unit tests
│
├── main.py              # CLI entry point
├── README.md
└── .gitignore
```

## Installation

1. Clone the repository:

```
git clone https://github.com/leonitaas/gradebook-cli.git
cd gradebook-cli
```

2. Ensure Python is installed (Python 3.10+ recommended)

## Usage

### Seed initial data

```
python -m scripts.seed
```

### List data

```
python main.py list students
python main.py list courses
python main.py list enrollments
```

### Add a student

```
python main.py add-student --name "John Doe"
```

### Add a course

```
python main.py add-course --code CS102 --title "Algorithms"
```

### Enroll a student

```
python main.py enroll --student-id 1 --course CS101
```

### Add a grade

```
python main.py add-grade --student-id 1 --course CS101 --grade 90
```

### Compute average grade

```
python main.py avg --student-id 1 --course CS101
```

### Compute GPA

```
python main.py gpa --student-id 1
```

## Testing

Run unit tests using:

```
python -m unittest discover tests
```

## Technologies Used

* Python
* argparse (CLI interface)
* JSON (data storage)
* unittest (testing framework)

## Key Concepts Demonstrated

* Modular architecture (separation of concerns)
* Command-line interface design
* Data validation and error handling
* Persistent storage handling
* Test-driven development basics


## Author

Leonita Sinani
