# Dictionary to store user information
user_info = {}

def add_user(name, age):
    """Add user information to the dictionary."""
    user_info[name] = age
    print(f"User {name} added successfully.")

def retrieve_user(name):
    """Retrieve user information by name."""
    if name in user_info:
        print(f"{name} is {user_info[name]} years old.")
    else:
        print(f"No information found for {name}.")

def main():
    while True:
        action = input("Would you like to add a user or retrieve information? (add/retrieve/exit): ").strip().lower()
        if action == 'add':
            name = input("Enter the user's name: ")
            age = int(input("Enter the user's age: "))
            add_user(name, age)
        elif action == 'retrieve':
            name = input("Enter the name to retrieve information: ")
            retrieve_user(name)
        elif action == 'exit':
            print("Exiting the program.")
            break
        else:
            print("Invalid action. Please choose 'add', 'retrieve', or 'exit'.")

if __name__ == "__main__":
    main()
