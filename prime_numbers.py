for i in range(1,100):
	if i == 1:
		continue
	q = 0
	for j in range(1,i + 1):
		if i % j == 0:
			q += 1
	if q > 2:
		continue
	else:
		print(i)
		
