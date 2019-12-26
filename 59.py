#Заданы M строк, которые вводятся с клавиатуры. 
#Подсчитать количество пробелов в каждой из строк.

import re
M=3
list.strings=[]
for i in range(0,M):
print("vvedite stroku:",end=' ')
list.strings.append(input())
for string in list_strings:
count_spaces=len(re.findall(r'\s',string))
print("v stroke \"%s\"%s probelov" %(string,count_spaces))
