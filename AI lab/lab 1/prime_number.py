#Write a program to find prime number with in a range using function.

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True

start = int(input("Input first part of range: "))
end = int(input("Second Part of the range: "))

prime_numbers = []
for i in range(start, end + 1):
    if is_prime(i):
        prime_numbers.append(i)

print("Prime numbers between", start, "and", end, "are:")
print(prime_numbers)