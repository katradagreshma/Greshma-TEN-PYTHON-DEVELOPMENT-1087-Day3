# Task 1 - Number Pattern Generator

n = int(input("Enter the value of n: "))

# 1. Right Triangle of Stars
print("\n--- 1. Right Triangle of Stars ---")
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# 2. Inverted Triangle of Numbers
print("\n--- 2. Inverted Triangle of Numbers ---")
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# 3. Pascal's Triangle
print("\n--- 3. Pascal's Triangle (First", n, "rows) ---")
for i in range(n):
    row = []
    accumulator = 1
    for j in range(i + 1):
        row.append(accumulator)
        accumulator = accumulator * (i - j) // (j + 1)
    print(" " * (n - i), end="")
    print(" ".join(str(x) for x in row))

# 4. Prime Numbers up to n
print("\n--- 4. Prime Numbers up to", n, "---")
print("Prime numbers: ", end="")
for num in range(2, n + 1):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=" ")
print()
