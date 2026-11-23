

def calculate_average(grades):
    if not grades:
        return 0

    for grade in grades:
        if not isinstance(grade, (int, float)) or isinstance(grade, bool):
            raise ValueError("Grades must be numbers")

        if grade < 0 or grade > 100:
            raise ValueError("Grades must be between 0 and 100")

    return sum(grades) / len(grades)



def get_letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def generate_report(name, grades):
    average = calculate_average(grades)
    letter = get_letter_grade(average)

    if average >= 50:
        status = "Pass"
    else:
        status = "Fail"

    return {
        "name": name,
        "average": average,
        "letter": letter,
        "status": status
    }


def find_highest_grade(grades):
    highest = 0
    for grade in grades:
        if grade > highest:
            highest = grade
    return highest



def find_lowest_grade(grades):
    if not grades:
        return None

    return min(grades)
