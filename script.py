# Lab1/script.py

def calculate_age():
    try:
        birth_year = int(input("Enter your birth year: "))
    except ValueError:
        print("Please enter an integer for the birth year.")
        return

    current_year = 2024
    age = current_year - birth_year
    return age

def helloWorld():
    print('Hello World')

# Test the functions
print("Your age is:", calculate_age())
helloWorld()
