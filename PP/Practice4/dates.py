# dates.py
# Practice 4: Python Date Operations

from datetime import datetime, timedelta

print("\n" + "=" * 70)
print(" " * 20 + "PYTHON DATE OPERATIONS")
print("=" * 70 + "\n")

# ============================================================================
# TASK 1: Subtract 5 days from current date
# ============================================================================

print("TASK 1: Subtract 5 days from current date")
print("-" * 70)

current_date = datetime.now()
five_days_ago = current_date - timedelta(days=5)

print(f"Current date:   {current_date.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"5 days ago:     {five_days_ago.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Difference:     5 days")
print("\n" + "=" * 70 + "\n")

# ============================================================================
# TASK 2: Print yesterday, today, tomorrow
# ============================================================================

print("TASK 2: Print yesterday, today, tomorrow")
print("-" * 70)

today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print(f"Yesterday: {yesterday.strftime('%A, %B %d, %Y')}")
print(f"Today:     {today.strftime('%A, %B %d, %Y')}")
print(f"Tomorrow:  {tomorrow.strftime('%A, %B %d, %Y')}")
print("\n" + "=" * 70 + "\n")

# ============================================================================
# TASK 3: Drop microseconds from datetime
# ============================================================================

print("TASK 3: Drop microseconds from datetime")
print("-" * 70)

current_time = datetime.now()
without_microseconds = current_time.replace(microsecond=0)

print(f"With microseconds:    {current_time}")
print(f"Without microseconds: {without_microseconds}")
print("\n" + "=" * 70 + "\n")

# ============================================================================
# TASK 4: Calculate date difference in seconds
# ============================================================================

print("TASK 4: Calculate date difference in seconds")
print("-" * 70)

# Example dates
date1 = datetime(2026, 3, 1, 12, 0, 0)
date2 = datetime(2026, 2, 25, 8, 30, 0)

print(f"Date 1: {date1.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Date 2: {date2.strftime('%Y-%m-%d %H:%M:%S')}")

difference = date1 - date2
total_seconds = difference.total_seconds()

print(f"\nTime difference: {difference}")
print(f"Total seconds: {int(total_seconds)}")
print(f"Total minutes: {int(total_seconds / 60)}")
print(f"Total hours: {int(total_seconds / 3600)}")
print(f"Total days: {difference.days}")
print("\n" + "=" * 70 + "\n")

# ============================================================================
# BONUS: Interactive date difference calculator
# ============================================================================

print("BONUS: Interactive Date Difference Calculator")
print("-" * 70)
print("Calculate the difference between two dates\n")

try:
    # First date
    print("Enter first date:")
    year1 = int(input("  Year (YYYY): "))
    month1 = int(input("  Month (1-12): "))
    day1 = int(input("  Day (1-31): "))
    
    # Second date
    print("\nEnter second date:")
    year2 = int(input("  Year (YYYY): "))
    month2 = int(input("  Month (1-12): "))
    day2 = int(input("  Day (1-31): "))
    
    # Calculate
    date1 = datetime(year1, month1, day1)
    date2 = datetime(year2, month2, day2)
    
    diff = abs((date1 - date2).total_seconds())
    days = int(diff / 86400)
    
    print(f"\nResults:")
    print(f"  Total seconds: {int(diff)}")
    print(f"  Total days: {days}")
    print(f"  Total weeks: {days // 7}")
    print(f"  Total years: {days // 365}")
    
except ValueError as e:
    print(f"Invalid date input: {e}")

print("\n" + "=" * 70)
print(" " * 25 + "All tasks completed!")
print("=" * 70 + "\n")