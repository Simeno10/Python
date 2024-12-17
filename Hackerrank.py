class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNum, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNum = idNum
        self.scores = scores
    def printPerson(self):
        print("Name:", lastName+",", firstName)
        print("ID:", idNum)
    def calculate(self):
        sumi = 0
        for i in range(len(scores)):
            sumi += scores[i]
        score = int(sumi/len(scores))
        if (score>=90):
            return "O"
        elif (score>=80 and score<90):
            return "E"
        elif (score>=70 and score<80):
            return "A"
        elif (score>=55 and score<70):
            return "P"
        elif (score>=40 and score<55):
            return "D"
        else:
            return "T"


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
