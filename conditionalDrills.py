'''
For this assignment you should read the task, then below the task do what it asks you to do.
'''

'''
#1) Create a Variable called grade and set it to an integer. Make an if statement that checks if the grade is a passing grade. grade must be above 65 to pass. print out "student is passing"
'''
grade = 80
if(grade>65):
    print("Student is passing")
else:
    print("Student is failing")
'''
#2) Now make an if, else statement that checks if the student is passing but also print "student is failing", if the grade is less than 65
'''
grade = 40
if(grade>65):
    print("Student is passing")
else:
    print("Student is failing") 
'''
#3)Create a variable called age. Make and if, else statement that checks if the age entered is old enough to vote. Remember the voting age is 18
'''
age = 16
if(age>=18):
    print("Can vote")
else:
    print("Cannot vote")
'''
#4)Create a variable called weight. If weight is an integer, assume it's in kilograms and convert it to pounds 
'''
weight = 10
if type(weight) == int:
    print("The weight is " + str(weight*2.205) + " lbs")
'''
#5)Now modify the previous program to also convert from pounds to kilograms
'''
weight = 170
if type(weight) == int:
    print("The weight is " + str(weight/2.205) + " kg")
'''
#6)create a list (seat1 = 1, seat2 = 1, seat3 = 0, seat4 = 1), Now make an if elseif, else statement that checks if a seat is open. if the seat = 1 its closed and print that it's closed. If the seat = 0, it's open and print that it's open. If no seats are open print "There are no available seats"
'''
seats = [1,1,0,1]
if(seats[0]  == 0):
    print("Seat 1 is available")
else:
    print("Seat 1 is not available")
if(seats[1] == 0):
    print("Seat 2 is available")
else:
    print("Seat 2 is not available")
if(seats[2] == 0):
    print("Seat 3 is available")
else:
    print("Seat 3 is not available")
if(seats[3] == 0):
    print("Seat 4 is available")
else:
    print("Seat 4 is not available")
if seats == [1,1,1,1]:
    print("No seats are available")    
    