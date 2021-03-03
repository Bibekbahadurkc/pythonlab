#A school decided to replace the desks in three classrooms. Each desk sits two students.Given the number of students in each class, print the smallest possible number of desks that can be purchased.
#The program should read three integers: the number of students in each of the three classes, a, b and c respectively.
#In the first test there are three groups.The first group has 20 students and thus needs 10 desks.The second group has students, so we need   desks in total.

#no_students_Class1 = int(input("Enter the number of student in first class : "))
#no_students_Class2 = int(input("Enter the number of student in Second class : "))
#no_students_Class3 = int(input("Enter the number of student in third class : "))

#desk_class1 = (no_students_Class1 // 2)
#print(f"The required number of desk for first class is {desk_class1}")
#desk_class2 = (no_students_Class1 // 2)
#print(f"The required number of desk for first class is {desk_class2}")
#desk_class3 = (no_students_Class1 // 2)
#print(f"The required number of desk for first class is {desk_class3}")

#total_desk = desk_class1 + desk_class2 + desk_class3
#print(f"Total number of desks that can be purchased is {total_desk}")

n1 = int(input("enter student class 1"))
n2 = int(input("enter student class 1"))
n3 = int(input("enter student class 1"))

total = n1 + n2 + n3
if total % 2==0:
    desk = total/2
    print(f"Desk{Desk}")
else:
    desk = ((total+1)/2)
    print(f"Desk{desk}")