def get_user_input():
    while True:
        try:
            number = int(input("Please enter a number: "))
            print(f"You entered: {number}")
            break  # Exit the loop if input is valid
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    get_user_input()
