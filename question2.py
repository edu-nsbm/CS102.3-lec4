# Q: Write a program to check if a person is eligiable to vote. (age: 18)


def main() -> None:
    while True:
        try:
            age: int = int(input("Enter your age: "))
            break
        except ValueError:
            print("Invalid value! Retry.")

    if age >= 18:
        print("You're eligiable")
    else:
        print("You're not eligiable")


if __name__ == "__main__":
    main()
