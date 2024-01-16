print("Hi, we are going to calculate GPA of your students.")

# take input from user for student grades
student1 = input("Please input the grade of your first student ")

student2 = input("Please input the grade of your second student ")

student3 = input("Please input the grade of your third student ")

# convert student grades from strings to intergers
student1 = int(student1)
student2 = int(student2)
student3 = int(student3)

# calculatee the average of students
average = float(student1 + student2 + student3)/3

# pass average back into a string so it csn be used in a print function
answer = str(average)

print("Your class average is " + answer)











