import math
X = input (' введите значение X ')
Y = input (' введите значение Y ')
 if X > Y :
	Z = math.sqrt(X * Y)
	print ( Z , '= ')
else :
	Z = math.log(X + Y, math.e)
	print ( Z , '= ')
