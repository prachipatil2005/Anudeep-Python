# Accept student name as key and marks as value
student_marks={}
n=int(input("Enter the number of students:"))
# Accept student name and marks
for _ in range(n):
    name=input("Enter student Name:")
    marks=float(input(f"Enter a marks for:{name}:"))
    student_marks[name]=marks
# Calculate mean of the marks
mean_marks=sum(student_marks.values())/len(student_marks)
print(f"The mean of the marks is:{mean_marks}")