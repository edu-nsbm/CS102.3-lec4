# When student enters the marks, provide the grade based on following criteria.
# Makrs     |     Grade
# >= 75     |     A
# >= 65     |     B
# >= 55     |     C
# >= 40     |     S
# < 40      |     F


def grade_marks(marks: float) -> str:
    if marks >= 75:
        return "A"
    elif marks >= 65:
        return "B"
    elif marks >= 55:
        return "C"
    elif marks >= 40:
        return "S"
    else:
        return "F"


def main() -> None:
    while True:
        try:
            marks: float = float(input("Enter your marks: "))
            break
        except ValueError:
            print("Invalid value! Retry.")

    if marks >= 0 and marks <= 100:
        print(f"Your grade is: {grade_marks(marks)}")
    else:
        print("Invalid marks.")


if __name__ == "__main__":
    main()
