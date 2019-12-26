#Заданы M строк символов, которые вводятся с клавиатуры. Найти количество символов в самой длинной строке.
#Выровнять строки по самой длинной строке, поставив перед каждой строкой соответствующее количество звёздочек.

import random
M=random.randint(1,10)
arr=[random.randint(1,10) for i in range(M)]
for i in range(M):
    arr[i]=input()
print(arr)
print("количество символов в самой длинной строке:" + str(len(max(arr))))
K=len(max(arr))
for i in range(M):
    N=K-len(arr[i])
    print("*" * N + str(arr[i]))
