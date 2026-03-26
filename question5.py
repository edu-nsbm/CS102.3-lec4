# Write a program to calculate the electricity bill of a house when consumed units entered according to following criteria.


def calculate_base_cost(units_count: float) -> float:
    if units_count <= 50:
        return units_count * 10
    elif units_count <= 90:
        return 50 * 10 + (units_count - 50) * 15
    else:
        return 50 * 10 + 40 * 15 + (units_count - 90) * 50


def main() -> None:
    while True:
        try:
            units_count: float = float(input("Enter units count: "))
            break
        except ValueError:
            print("Invalid value. Retry")

    if units_count >= 0:
        base_cost: float = calculate_base_cost(units_count)
        full_cost = base_cost + 1000.0

        print(f"Your full cost is: {full_cost}")
    else:
        print("Invalid value. Retry")


if __name__ == "__main__":
    main()
