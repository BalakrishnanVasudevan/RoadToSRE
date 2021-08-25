for i in range(1,101):
	if (i%3==0) or (i%5==0):
		if (i%3==0) and (i%5==0):
			print("FizzBuzz")
		elif (i%3==0):
			print("Fizz")
		else:
			print("Buzz")
	else:
		print(i)
