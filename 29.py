import random
A=random.randint(1, 2007)
print("year: " +str(A))
if A % 4 == 0:
	print(str(A) + "year a leap")
elif not A % 4 ==0:
print(str(A) + "year a not leap")
V= A//100+1
print(str(A)+ "year, " + str(V) + "century")
