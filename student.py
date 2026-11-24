class Student:

    def __init__(self, studentID, firstName, lastName, email, age):
        self.studentID = studentID
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.age = age

    def getDetails(self):
        return f"Student ID: {self.studentID}\nName: {self.firstName} {self.lastName}\nEmail: {self.email}\nAge: {self.age}"

    def updateEmail(self, email):
        self.email = email


student1 = Student(1001, "Ahmet", "Yilmaz", "ahmet@gmail.com", 21)

print(student1.getDetails())

student1.updateEmail("ahmetnew@gmail.com")

print("\nUpdated Student Information:")
print(student1.getDetails())