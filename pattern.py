while True:
	num = int(input("Enter a number:"))
	if num > 0:
		break
def print_pattern(num):
	print(f"Input number is : {num}")
	a = 1
	while a <= num + 1:
		for i in range(1, a):
			print(i, end = " ")
		print()
		a += 1
print_pattern(num)
