# generators.py
# Practice 4: Python Iterators and Generators

print("=" * 60)
print("PYTHON GENERATORS - ALL TASKS")
print("=" * 60 + "\n")

# ============================================================================
# TASK 1: Generator for squares up to N
# ============================================================================

def square_generator(N):
    """Generator that yields squares of numbers from 1 to N"""
    for i in range(1, N + 1):
        yield i ** 2

print("TASK 1: Squares up to N")
print("-" * 60)
N = 8
print(f"Squares from 1 to {N}:")
for square in square_generator(N):
    print(square, end=" ")
print("\n" + "=" * 60 + "\n")

# ============================================================================
# TASK 2: Even numbers from 0 to n (comma separated)
# ============================================================================

def even_numbers(n):
    """Generator that yields even numbers from 0 to n"""
    for i in range(0, n + 1, 2):
        yield i

print("TASK 2: Even numbers (comma separated)")
print("-" * 60)
n = int(input("Enter a number: "))
result = ",".join(map(str, even_numbers(n)))
print(f"Even numbers from 0 to {n}: {result}")
print("=" * 60 + "\n")

# ============================================================================
# TASK 3: Numbers divisible by 3 AND 4
# ============================================================================

def divisible_by_3_and_4(n):
    """Generator for numbers divisible by both 3 and 4 (divisible by 12)"""
    for i in range(0, n + 1, 12):
        yield i

print("TASK 3: Numbers divisible by 3 AND 4")
print("-" * 60)
n = int(input("Enter the range limit: "))
print(f"Numbers divisible by 3 AND 4 between 0 and {n}:")
for num in divisible_by_3_and_4(n):
    print(num, end=" ")
print("\n" + "=" * 60 + "\n")

# ============================================================================
# TASK 4: Squares from a to b
# ============================================================================

def squares(a, b):
    """Generator that yields squares of all numbers from a to b"""
    for i in range(a, b + 1):
        yield i ** 2

print("TASK 4: Squares from a to b")
print("-" * 60)
a, b = 3, 9
print(f"Squares from {a} to {b}:")
for square in squares(a, b):
    print(f"{square}", end=" ")
print("\n" + "=" * 60 + "\n")

# ============================================================================
# TASK 5: Countdown from n to 0
# ============================================================================

def countdown(n):
    """Generator that yields all numbers from n down to 0"""
    for i in range(n, -1, -1):
        yield i

print("TASK 5: Countdown from n to 0")
print("-" * 60)
n = int(input("Enter starting number: "))
print(f"Countdown from {n} to 0:")
for num in countdown(n):
    print(num, end=" ")
print("\n" + "=" * 60 + "\n")

print("All tasks completed!")