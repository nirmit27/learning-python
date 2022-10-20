#Checking for Prime number

a = int(input('Enter the number:\t'))
def primeOrNot(a):
	if a>1:
		for i in range(2,int(a**0.5)+1) :
			if (a%i==0) :
				print('{} is not prime.'.format(a))
				break
		else :
			print('{} is prime.'.format(a))
primeOrNot(a)