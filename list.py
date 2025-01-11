def calculate_sum_and_average(numbers):
    """Calculate the sum and average of a list of numbers."""
    if not numbers:  # Check if the list is empty
        return "The list is empty. Please provide valid numbers."

    total = sum(numbers)  # Calculate the sum
    average = total / len(numbers)  # Calculate the average

    return total, average


# Get input from the user
try:
    user_input = input("Enter a list of numbers separated by spaces: ")
    numbers = list(map(float, user_input.split()))  # Convert input to a list of numbers

    if not numbers:  # Check if the list is empty after processing
        print("You didn't enter any numbers.")
    else:
        total, average = calculate_sum_and_average(numbers)
        print(f"The sum of the numbers is: {total}")
        print(f"The average of the numbers is: {average}")
except ValueError:
    print("Invalid input. Please enter numbers only.")
