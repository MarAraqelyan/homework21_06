ls1 = [1, 2, 3, 4, 5, 6]
ls2 = [3, 6, 1, 2, 7, 0, 6, 3, 2]
ls = []

def find_common_elements(a,b):
	for i in a:
		if i in b:
			ls.append(i)
	set(ls)		
	print(ls)

find_common_elements(ls1, ls2)
