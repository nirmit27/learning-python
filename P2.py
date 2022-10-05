a = int(input('Enter the number:	'))
if a>1:
	for i in range(2,int(a**0.5)+1) :
		if (a%i==0) :
			print('Number {} is not prime'.format(a))
			break
	else :
		print('Number {} is prime'.format(a))