import json

# Read JSON file
def read_json(file_path):
    """Read JSON data from a file."""
    with open(file_path, 'r') as file:
        return json.load(file)

def main():
    # Prompt user for JSON file path
    file_path = input("Enter the path to the JSON file: ").strip()

    # Load the JSON data
    try:
        data = read_json(file_path)
    except Exception as e:
        print(f"Error: {e}")
        return

    # Prompt user for input
    day = int(input("Enter the day number (1-12) to get details: "))

    # Find and print the corresponding information
    for entry in data['progress']:
        if entry['day'] == day:
            print(f"Day {entry['day']}: {entry['topic']}")
            print(f"Notes: {entry['notes']}")
            break
    else:
        print("Invalid day number. Please enter a number between 1 and 12.")

if __name__ == "__main__":
    main()
