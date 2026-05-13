# Student Marks & Grade Calculator

# Ask user to enter their name
name = input("Enter your name: ")

# Ask user to enter Maths marks
math_marks = int(input("Enter your Maths marks: "))

# Ask user to enter Computer marks
computer_marks = int(input("Enter your Computer marks: "))

# Ask user to enter Physics marks
physics_marks = int(input("Enter your Physics marks: "))

# Total marks
total_marks = 300

# Calculate obtained marks
obtained_marks = math_marks + computer_marks + physics_marks

# Calculate percentage
percentage = (obtained_marks / total_marks) * 100

# Display student details
print("\n========== RESULT ==========")
print("Student Name:", name)
print("Obtained Marks:", obtained_marks)
print("Percentage:", percentage, "%")

# Check grade according to percentage
if percentage > 80:
    print("Status: PASS")
    print("Grade: A")

elif percentage > 60:
    print("Status: PASS")
    print("Grade: B")

elif percentage > 40:
    print("Status: PASS")
    print("Grade: C")

else:
    print("Status: FAIL")