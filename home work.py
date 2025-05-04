# Define a list of 15 numbers
numbers = list(range(1, 16))

# Loop through the list and determine if the number is odd or even
for number in numbers:
    if number % 2 == 0:
        print(str(number) + " is even")
    else:
        print(f"{number} is odd")
