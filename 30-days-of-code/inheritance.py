class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self,firstName,lastName,idNumber,scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores

    def calculate(self):
        grade = ''
        avg = sum(self.scores)/len(self.scores)
        if(90 <= avg <= 100):
            grade = 'O'
        elif (80 <= avg < 90):
            grade = 'E'
        elif (70 <= avg < 80):
            grade = 'A'
        elif (55 <= avg < 70):
            grade = 'P'
        elif (40 <= avg < 55):
            grade = 'D'
        elif (avg < 40):
            grade = 'T'
        return grade
