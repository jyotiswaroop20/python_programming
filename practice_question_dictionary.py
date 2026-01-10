#Wrtite a program to accept a marks from user and store it in a dictionary and print
#the dictionary
marks_dict = {}
n = int(input("Enter number of subjects: "))
for _ in range(n):
    subject = input("Enter subject name: ")
    marks = int(input("Enter marks obtained: "))
    marks_dict[subject] = marks

print("Marks Dictionary:", marks_dict)

# Another method to create and print dictionary
my_dict = {}

m1 = int(input("Enter marks for subject 1: "))
my_dict.update({"subject1": m1})

m2 = int(input("Enter marks for subject 2: "))
my_dict.update({"subject2": m2})

m3 = int(input("Enter marks for subject 3: "))
my_dict.update({"subject3": m3})