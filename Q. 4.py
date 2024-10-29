#4. Write a program to reverse a given number (e.g., 1234 becomes 4321) using a while loop.

# Input number to be reversed
num = 1234
reversed_num = 0  # Initialize reversed number to 0

# Loop until all digits are processed
while num > 0:

# calculate reversed number by shifting current digits to left and adding last digits of original number
    reversed_num = reversed_num * 10 + num % 10
    num //= 10  # Interger division (//) it discard remainder

print(reversed_num)  # Display the result of the reversed number