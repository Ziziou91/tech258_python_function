"""App to demonstrate function usage in Python."""


def addition(num_1: float, num_2: float) -> float:
    return num_1 + num_2


def subtraction(num_1: float, num_2: float) -> float:
    return num_1 - num_2


def multiplication(num_1: float, num_2: float) -> float:
    return num_1 * num_2


def division(num_1: float, num_2: float) -> float:
    return num_1 / num_2


def get_input(valid_input_type: str) -> str | float:
    user_input = None

    if valid_input_type == "operator":
        # Get operator and validate
        valid_inputs = ["+", "-", "*", "/"]
        print(f"\n{'-'*23}Choose operator{'-'*22}")
        print("Please choose one of the following operations:")
        for valid_operator in valid_inputs:
            print(f"\t{valid_operator}")
        user_input = input("Your input: ")

        valid_input = False
        while not valid_input:
            if user_input in valid_inputs:
                valid_input = True
            else:
                print(f"ERROR! {user_input} is not valid. Please try again.")
                user_input = input("Your input: ")

    elif valid_input_type == "number":
        # Get number and validate.
        print(f"\n{'-'*23}Choose number{'-'*22}")
        print("Please choose a number:")

        user_input = input("Your input: ")
        valid_input = False
        while not valid_input:
            try:
                float(user_input)
            except ValueError:
                print(f"ERROR! {user_input} is not valid. Please try again.")
                user_input = input("Your input: ")
            else:
                user_input = float(user_input)
                valid_input = True

    return user_input


def main() -> None:
    print(f"{'='*60}")
    print(f"{'*'*25}Calculator{'*'*25}")
    print(f"{'=' * 60}")

    # Get the user inputs
    user_operator = get_input("operator")
    num_1 = get_input("number")
    print(f"1st number - {num_1}")
    num_2 = get_input("number")
    print(f"2nd number - {num_2}")

    print(f"\n{'-' * 23}calculate!{'-' * 22}")
    print(f"Your calculation will be: {num_1} {user_operator} {num_2}")
    # route valid_input
    if user_operator == "+":
        print(addition(num_1, num_2))
    elif user_operator == "-":
        print(subtraction(num_1, num_2))
    elif user_operator == "*":
        print(multiplication(num_1, num_2))
    elif user_operator == "/":
        print(division(num_1, num_2))


if __name__ == "__main__":
    main()
