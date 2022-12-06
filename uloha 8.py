#Zisti, či je súčet dvoch posledných cifier párny

a = int(input('zadaj 2 a viac ciferne cislo '))
b = str(a)
c = int(b[-2])
d = int(b[-1])
e = c + d

if e%2 == 0:
    print('sucet poslednych 2 cisiel je parny ')
else:
    print('sucet poslednych 2 cisiel je neparny ')