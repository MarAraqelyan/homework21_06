while True:
	num = int(input("Enter a positive number:"))
	if num > 0:
		break
pfactors = []

def find_prime_factors(num):
	if num == 1:
		print("This number has no prime factors!")
	i = 2 
	while i <= num:
		if num % i == 0:
			pfactors.append(i)
			num = num / i
		else:
			i += 1
	return pfactors

print(find_prime_factors(num))


