def parse_grade(value):
    try:
        grade = float(value)
        if not (0 <= grade <= 100):
            raise ValueError
        return grade
    except:
        raise ValueError("Grade must be between 0 and 100")