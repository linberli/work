# Дано натуральное число. Определить, будет ли это число: чётным, кратным 10.
x = input (' введите число для проверки ')
>>> if x % 2 == 0 and x % 10 == 0 :
	print (' число ' , x , 'четное и кратное 10 ')
else :
	print (' число не соответсвует условию ')
