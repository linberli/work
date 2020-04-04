import numpy as np
import random
 
n = int(input('Введите количество строк: '))  
m = int(input('Введите количество столбцов: '))
 
matrix = np.zeros((n,m), dtype=np.integer)
for i in range(0,n):
    for j in range(0,m):
        r = random.randint(1,9)
        matrix[i,j] = r
print('\v\x1b[4;32mМатрица создана:\x1b[0m\n'+'\v\x1b[36m'+str(matrix)+'\x1b[0m\v\v')
"""\x1b[1;32mТекст\x1b[0m"""
 
matrix_div = np.zeros((n,m), dtype=np.float)
for x in range(0,m):
    column = matrix[:,x]
    mx = max(column)
    print('\x1b[32mМаксимальное число в колонке №\x1b[0m '+'\x1b[1;34m'+str(x+1)+'\x1b[0m'+' = \x1b[1;31m'+str(mx)+'\x1b[0m')
    column = [divide / mx for divide in column]
    matrix_div[:,x] = column
