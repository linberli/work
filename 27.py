a = input (' введите значение a')
>>> x = a
>>> if x <= 0 :
	fx = 0
	print ( fx, '= ')
elif 0<x<1 :
	fx = x ** 2 - x
	print ( fx, '= ')
else :
	fx = x ** 2 - sin( math.pi * x ** 2)
	print (fx , '= ')
