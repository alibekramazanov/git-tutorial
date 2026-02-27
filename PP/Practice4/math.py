# math_operations.py
# Practice 4: Python Math Operations

import math

print("\n" + "=" * 70)
print(" " * 20 + "PYTHON MATH OPERATIONS")
print("=" * 70 + "\n")

# ============================================================================
# TASK 1: Convert degree to radian
# ============================================================================

print("TASK 1: Convert degree to radian")
print("-" * 70)

degree = float(input("Input degree: "))
radian = math.radians(degree)

print(f"Output radian: {radian:.6f}")
print(f"\nFormula used: radian = degree × (π / 180)")
print(f"Calculation: {degree} × (π / 180) = {radian:.6f}")
print("\n" + "=" * 70 + "\n")

# ============================================================================
# TASK 2: Calculate area of trapezoid
# ============================================================================

print("TASK 2: Calculate area of trapezoid")
print("-" * 70)

height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))

area_trapezoid = ((base1 + base2) / 2) * height

print(f"Expected Output: {area_trapezoid}")
print(f"\nFormula: Area = ((base1 + base2) / 2) × height")
print(f"Calculation: (({base1} + {base2}) / 2) × {height} = {area_trapezoid}")
print("\n" + "=" * 70 + "\n")

# ============================================================================
# TASK 3: Calculate area of regular polygon
# ============================================================================

print("TASK 3: Calculate area of regular polygon")
print("-" * 70)

n = int(input("Input number of sides: "))
side_length = float(input("Input the length of a side: "))

# Formula: Area = (n × side²) / (4 × tan(π/n))
area_polygon = (n * side_length ** 2) / (4 * math.tan(math.pi / n))

print(f"The area of the polygon is: {area_polygon:.0f}")
print(f"\nFormula: Area = (n × side²) / (4 × tan(π/n))")
print(f"where n = number of sides")
print("\n" + "=" * 70 + "\n")

# ============================================================================
# TASK 4: Calculate area of parallelogram
# ============================================================================

print("TASK 4: Calculate area of parallelogram")
print("-" * 70)

base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

area_parallelogram = base * height

print(f"Expected Output: {area_parallelogram}")
print(f"\nFormula: Area = base × height")
print(f"Calculation: {base} × {height} = {area_parallelogram}")
print("\n" + "=" * 70 + "\n")

# ============================================================================
# BONUS: Summary of all calculations
# ============================================================================

print("SUMMARY OF ALL CALCULATIONS")
print("-" * 70)
print(f"1. Degree to Radian: {degree}° = {radian:.6f} rad")
print(f"2. Trapezoid Area: {area_trapezoid}")
print(f"3. Polygon Area ({n} sides): {area_polygon:.0f}")
print(f"4. Parallelogram Area: {area_parallelogram}")
print("\n" + "=" * 70)
print(" " * 25 + "All tasks completed!")
print("=" * 70 + "\n")