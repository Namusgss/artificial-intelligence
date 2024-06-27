#Write a program to generate the Fibonacci sequence of a given number.

num = int(input("Enter a number: "))
a = 0
b = 1
fib = []
for i in range(num):
    fib.append(a)
    a, b = b, a + b
print("Fibonacci sequence of", num, "is:")
print(fib)