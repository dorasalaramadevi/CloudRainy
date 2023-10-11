# Initialize empty lists for numbers and words
numbers = []
words = []

# Collect numbers until "0" is entered
while True:
    user_input = input("Enter a number (0 to finish numbers): ")

    if user_input == "0":
        break
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a number.")

# Collect words until "END" is entered
while True:
    user_input = input("Enter a word (END to finish words): ")

    if user_input == "END":
        break
    words.append(user_input)

# Sort and print numbers
print("Numbers in ascending order:", sorted(numbers))
print("Numbers in descending order:", sorted(numbers, reverse=True))

# Sort and print words
print("Words in ascending order:", sorted(words))
print("Words in descending order:", sorted(words, reverse=True))
