import math

list = []
for i in range(11):
    m = math.factorial(6*i)
    m1 = math.factorial(3*i)
    m2 = math.factorial(i)
    M = m/(m1 *(m2**3))
    L = 545140134 * i + 13591409
    X = 262537412640768000 **i
    drob = (M * L)/X
    list.append(drob)

summa = 0
for chislo in (list):
    summa = summa + chislo
    C = 426880 * math.sqrt(10005)
    pi = C * (1/summa)
print (pi)


list1 = []
for i in range(11):
    a = 4 / (8 * i + 1)
    b = 2 / (8 * i + 4)
    c = 1 / (8 * i + 5)
    d = 1 / (8 * i + 6)
    abcd = a - b - c - d
    q = (16 ** (-i)) * abcd
    list1.append(q)
    summa1 = 0
    for chislo1 in (list1):
        summa1 = summa1 + chislo1
print (summa1)