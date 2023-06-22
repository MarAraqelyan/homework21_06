while True:
	num = int(input("Enter a positive number:"))
	if num >= 0:
		break
def find_factorial(num):
	if num == 0:
		pass
	factorial = 1
	while num >= 1:
		factorial *= num
		num -= 1
	return factorial

print(f"The factorial of {num} is {find_factorial(num)}" )




