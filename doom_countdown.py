import time
def countdown():
	number = 10
	while number > 0:
		print (number)
		time.sleep(0.5)
		number -= 1
	print ("DOOOM")

countdown()

