# Lab1/script.py

def calculate_age():
    birth_year = int(input("Enter your birth year: "))
    current_year = 2024  # You can update this to the current year
    age = current_year - birth_year
    return age

def helloWorld():
    print('Hello World')

# Test the functions
print("Your age is:", calculate_age())
helloWorld()
