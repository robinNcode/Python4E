'''
5.2 Write a program that repeatedly prompts a user for
integer numbers until the user enters 'done'. 
Once 'done' is entered,print out the largest and smallest of the numbers.
If the user enters anything other than a valid number catch it with
a try/except and put out an appropriate message and ignore the number.
'''

largest = None
smallest = None
error = False
	
while True :
	number = input("Enter a numnber:")
	
	try :
		number = int(number)
	except :
		error = True
	
	if number == "done" : break
	elif error == True :
		print("Invalid input")
		error = False
	elif type(number) != int:
		number = 0
	else :
		if largest == None  or smallest == None:
			largest = number
			smallest = number
		elif number >= largest:
			largest = number
		elif number <= smallest:
			smallest = number
			
print("Maximum is",largest)
print("Minimum is",smallest)
