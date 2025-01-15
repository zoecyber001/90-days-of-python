import math

def calculate_square_root(number):
    return math.sqrt(number)

if __name__ == "__main__":
    user_input = float(input("Enter a number to calculate its square root: "))
    result = calculate_square_root(user_input)
    print(f"The square root of {user_input} is {result}")
