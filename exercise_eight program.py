# Hello! This program prints a pattern of numbers using nested for loops.

# Loop from 1 to 10
for num in range(1, 11):
    # Loop from 1 to the current number
    for i in range(1, num + 1):
        # Print the current number
        print(num, end=" ")
    # Print a new line after each row to display the pattern correctly
    print()
    