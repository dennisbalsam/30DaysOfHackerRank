class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__ (self, firstName, lastName, idNumber, scores):
        Person.__init__(self,firstName,lastName,idNumber)
        self.scores = scores

    

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self): 
        average = 0

        # count up total of scores
        for i in self.scores:
            average += i
        
        # divide by amount of scores
        average /= len(self.scores)
        average =int(average)

        # find chracter grade
        if average in range(90,101):
            return 'O'
        elif average in range(80,90):
            return 'E'
        elif average in range(70,80):
            return 'A'
        elif average in range(55,70):
            return 'P'
        elif average in range(40,55):
            return 'D'
        else:
            return 'T'
    




line = input().split()