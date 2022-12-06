#Naprogramuj funkciu, ktorá po zadaní troch hodnôt vypíše, či hodnoty sú stranami trojuholníka a ak áno, tak akého (pravouhlého, rovnoramenného, rovnostranného ap.)

a = float(input('zadaj najdlhsiu stranu '))
b = float(input('zadaj najkratsiu stranu '))
c = float(input('zadaj poslednu stranu '))

if b <= a <= a and (b+c)>a:
    if a*a == (b*b + c*c):
        print('trojuholnik je pravouhly ')
    elif a == b == c :
        print('trojuholnik je rovnostranny ')
    elif a== c or a==b or b==c:
        print('trojuholnik je rovnoramenny ')
    else:
        print('trojuholnik je normalny')
else:
	print("cisla nie su stranami ani jednych z tychto druhov trojuholnikov ")


