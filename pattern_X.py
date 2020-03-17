# Printing 'X' Pattern gave in machine Test.

n = int(input(" Input-1 >>"))


for i in range(n):
	print('  '*i + '* ',end='')
	if i<(n-1) :
		print('  '*((2*n)-(2*i)-3) + '*')
	print()

	

for i in range(n-1):
	print()
	print('  '*((n-2)-i) + '* ',end='')
	if i>=0 :
		print('  '*(2*i+1) + '*')



	
