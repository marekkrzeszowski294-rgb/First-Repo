def get_number(prompt):
    """Ask the user for a number until they type a valid one."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please type a valid number.")


def calculate(first_number, operator, second_number):
    """Return the result for one calculation."""
    if operator == "+":
        return first_number + second_number
    elif operator == "-":
        return first_number - second_number
    elif operator == "*":
        return first_number * second_number
    elif operator == "/":
        if second_number == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return first_number / second_number
    elif operator == "**":
        return first_number ** second_number
    elif operator == "//":
        if second_number == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return first_number // second_number
    elif operator == "%":
        if second_number == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return first_number % second_number
    else:
        raise ValueError("Unknown operator.")


def show_menu():
    print("\n=== Smart Calculator ===")
    print("Operators: +  -  *  /  **  //  %")
    print("Type 'history' to see old calculations.")
    print("Type 'quit' to stop.")


def show_history(history):
    if not history:
        print("No calculations yet.")
        return

    print("\nCalculation history:")
    for item in history:
        print(item)


def run_calculator():
    history = []

    while True:
        show_menu()
        operator = input("Choose operator: ").strip().lower()

        if operator == "quit":
            print("Goodbye. Keep practicing.")
            break

        if operator == "history":
            show_history(history)
            continue

        first_number = get_number("First number: ")
        second_number = get_number("Second number: ")

        try:
            result = calculate(first_number, operator, second_number)
        except ValueError:
            print("Invalid operator. Try again.")
            continue
        except ZeroDivisionError as error:
            print(f"Error: {error}")
            continue

        calculation = f"{first_number} {operator} {second_number} = {result}"
        history.append(calculation)
        print(f"Result: {result}")


if __name__ == "__main__":
    run_calculator()
