A = input (' ребро куба ')
>>> H = input (' высота цилиндра ')
>>> R = input (' радиус цилиндра ')
>>> M = input (' объем  жидкости ')
>>> int Z = A ** 3
int D = (R ** 2) * H
if M <= Z :
    print (' вместится в кубическую емкость ')
else :
    if M <= D :
        print ( ' вместится в цилиндрическую емкость ')
    else :
        if M <= Z and M <= D :
            print (' вместится в обе ')
        else :
            print (' не вместится вообще ')
