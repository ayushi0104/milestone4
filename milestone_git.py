def fibonaccii(n):
	if n==1:
		print ("0")
	elif n==2:
		print ("0 1")
	elif n>2:
		first = 0
		second = 1
		i=2
		for i in range(2,n):
			successive = first + second
			print(successive)
			first = second
			second = successive