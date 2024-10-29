#4. Write a program to reverse a given number (e.g., 1234 becomes 4321) using a while loop.

num = 456789
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)