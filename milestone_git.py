def fibonaccii(n):
	first = 0
	second = 1
	for i in range(2,n):
		successive = first + second
		print(successive)
		first = second
		second = successive
	