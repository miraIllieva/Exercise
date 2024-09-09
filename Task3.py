# On the first line, you will receive a single number n.
# On the following n lines, you will receive integers.
# After that, you will be given one of the following commands:
# even, odd, negative, positive.
# Filter all the numbers that fit in the category (0 counts as a positive and even).
# Finally, print the result.

# Step 1: Read the number of integers
n = int(input())

# Step 2: Initialize a list to store the integers
numbers = []

# Step 3: Collect n integers from the user
for i in range(n):
    current_number = int(input())
    numbers.append(current_number)

# Step 4: Read the command
command = input()

# Step 5: Initialize an empty list for filtered numbers
filtered = []

# Step 6: Filter based on the command
if command == "even":
    # Append even numbers to the filtered list
    filtered = [number for number in numbers if number % 2 == 0]
elif command == "odd":
    # Append odd numbers to the filtered list
    filtered = [number for number in numbers if number % 2 != 0]
elif command == "negative":
    # Append negative numbers to the filtered list
    filtered = [number for number in numbers if number < 0]
elif command == "positive":
    # Append positive numbers (including 0) to the filtered list
    filtered = [number for number in numbers if number >= 0]

# Step 7: Print the filtered numbers
print(filtered)
