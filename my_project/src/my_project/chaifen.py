# Python3 implementation of the approach

# Function that prints 
# the required sequence
def split(x, n):

	# If we cannot split the 
	# number into exactly 'N' parts
	if(x < n): 
		print(-1)

	# If x % n == 0 then the minimum 
	# difference is 0 and all 
	# numbers are x / n
	elif (x % n == 0):
		for i in range(n):
			print(x//n, end =" ")
	else:
		# upto n-(x % n) the values 
		# will be x / n 
		# after that the values 
		# will be x / n + 1
		zp = n - (x % n)
		pp = x//n
		for i in range(n):
			if(i>= zp):
				print(pp + 1, end =" ")
			else:
				print(pp, end =" ")
	
# Driver code		 
num = int(input("请输入一个大于50000且小于10000000的自然数："))
n = int(input("请输入要拆分的个数"))
n = 3
split(num, n)
