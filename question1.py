def find_larger_value(num1: int, num2: int) -> int:
    if num1 >= num2:
        return num1
    else:
        return num2


def main() -> None:

    while True:
        try:
            num1: int = int(input("Enter num1: "))
            num2: int = int(input("Enter num2: "))
            break
        except ValueError:
            print("Invalid input! Retry.")

    larger_value: int = find_larger_value(num1, num2)
    print(f"Larger value: {larger_value}")


if __name__ == "__main__":
    main()
