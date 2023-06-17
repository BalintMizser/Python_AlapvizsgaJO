print('1. feladat: A háromszög szerkesztethetősége')
print('Kérem a háromszög oldalait!')
a=float(input('a = '))
b=float(input('b = '))
c=float(input('c = '))
if a+b>c and a+c>b and b+c>a:
    print('A háromszög megszerkeszthető!')
else:
    print('A háromszög nem megszerkeszthető a megadott adatokkal!')