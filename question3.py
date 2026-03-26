# Finding the largest value of three numbers.


def find_largest(num1: int, num2: int, num3: int) -> int:
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


def find_largest_nested(num1: int, num2: int, num3: int) -> int:
    if num1 >= num2:
        if num1 >= num3:
            return num1
        else:
            return num3
    else:
        if num2 >= num3:
            return num2
        else:
            return num3


def main() -> None:
    while True:
        try:
            num1: int = int(input("Enter number 1: "))
            num2: int = int(input("Enter number 2: "))
            num3: int = int(input("Enter number 3: "))

            break
        except ValueError:
            print("Invalid value! Try again.")

    largest_num: int = find_largest_nested(num1, num2, num3)
    largest_num2: int = max(num1, num2, num3)
    largest_num3: int = find_largest(num1, num2, num3)

    print(f"The largest value is (nested if): {largest_num}")
    print(f"The largest value is (max): {largest_num2}")
    print(f"The largest value is (if-else-if): {largest_num3}")


if __name__ == "__main__":
    main()
