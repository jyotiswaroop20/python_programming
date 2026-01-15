class Student:
    college_name = "ABC College"

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def get_average(self):
        sum = 0
        for val in self.marks:
            sum += val
        print ("Hi", self.name, "Your average marks is", round(sum/3,2))


s1 = Student("Aditya Tripathi", [99,98,88,89])
s1.name = "Manoj" # we can change attribute value directly
s1.get_average()
# print(Student.college_name)

s2 = Student("Priyanka", [67,66,65,43])
s2.get_average()