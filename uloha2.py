#Naprogramuj funkciu, ktorá zistí, či dané číslo x patrí do intervalu <a,b>.

a = int(input('napis spodne cislo intervalu '))
b = int(input('napis vrchne cislo intervalu '))
x = int(input('napis cislo ktore ma patrit intervalu '))

if a < x < b:
    print('cislo je v intervale')
else:
    print('cislo nie je v intervale')



