# Create a Python program that repeatedly prompts the user for a number until a valid integer is provided.
# Use a try/except block to handle any ValueError exceptions, and keep asking for input until a valid integer is entered.
# Display the final valid integer.

while True:
    try:
        number = int(input('Enter number: '))
    except ValueError as error:
        print(error)
    else:
        print(f'Valid number: {number}')
        break
