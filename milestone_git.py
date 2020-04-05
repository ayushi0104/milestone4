def fibonaccii(n):
	if n==1:
		print ("Fibonacci Series :\n0 ")
	elif n==2:
		print ("Fibonacci Series :\n 0 \n 1")
	elif n>2:
		print ("Fibonacci Series : \n 0 \n 1 ")
		first = 0
		second = 1
		i=2
		for i in range(2,n):
			successive = first + second
			print(successive)
			first = second
			second = successive
n=int(input("Enter the range : "))
fibonaccii(n)