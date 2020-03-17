# Printing 'A' Pattern gave in machine Test.
import math as m

n = int(input(" Input-1 >>"))

for i in range(n):
	if n%2!=0:
		if i==m.floor(n/2):
			print('  '*((n-1)-i) + '* '*(n))
		else:
			print('  '*((n-1)-i) + '* ',end='')
			if i>=1 and i!=m.floor(n/2) :
				print('  '*(2*i-1) + '*')
	else:
		if i==m.floor(n/2):
			print('  '*((n-1)-i) + '* '*(n+1))
		else:
			print('  '*((n-1)-i) + '* ',end='')
			if i>=1 and i!=m.floor(n/2) :
				print('  '*(2*i-1) + '*')
	print()