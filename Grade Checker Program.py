# Grade Checker Program

# Take input from the user
score = int(input("Enter your score (0-100): "))

# Check grade using if-else
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

# Display the result
print(f"Your grade is: {grade}")
