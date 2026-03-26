# Write a program to calculate a water bill of a house when consumed units entered according to follolwing criteria,
#
# Unit Range     |     Cost per unit
# 0-30           |     5
# 31-60          |     10
# 61-100         |     15
# more than 100  |     50


def calculate_water_bill(units_count: int) -> int:
    if units_count <= 30:
        return units_count * 5 + 500
    elif units_count <= 60:
        return 30 * 5 + (units_count - 30) * 10 + 500
    elif units_count <= 100:
        return 30 * 5 + 30 * 10 + (units_count - 60) * 15 + 500
    else:
        return 30 * 5 + 30 * 10 + 40 * 15 + (units_count - 100) * 50 + 500


def main() -> None:
    while True:
        try:
            units_count: int = int(input("Enter water units count: "))
            break
        except ValueError:
            print("Invalid value. Retry.")

    if units_count >= 0:
        bill: int = calculate_water_bill(units_count)
        print(f"Your water bill is: {bill}")
    else:
        print("Units count cannot be negative. Restart")


if __name__ == "__main__":
    main()
