while True:

	a = (input("Enter the first number:"))
	op = input("Choose the operation - (+, -, *, /):")
	b = (input("Enter the second number:"))

	if '.' in a:
		a  = float(a)
	else:
		a = int(a)

	if '.' in b:
		b  = float(b)
	else:
		b = int(b)
	
	if op =='+':
		print(f"{a} + {b} = {a + b}")
	elif op =='-':
		print(f"{a} - {b} = {a - b}")
	elif op =='*':
		print(f"{a} * {b} = {a * b}")
	elif op =='/':
		if b == 0:
			print("Can't divide on zero!")
		else:
			print(f"{a} / {b} = {a / b}")

	answer = input("Do you want to exit, yes/no:")

	if answer == "yes":
		break
 
	
	


