from Eredmeny import *

eredmenyek : list[Eredmeny] =[]

file = open('ub2017egyeni.txt', 'r', encoding='utf-8')
file.readline()
for sor in file:
    eredmenyek.append(Eredmeny(sor.strip()))
file.close

print(f'3.2 feladat: Futók száma: {len(eredmenyek)}')

noiDarab = 0
for item in eredmenyek:
    if item.kategoria == 'Noi' and item.szazalek == 100:
        noiDarab +=1
print(f'3.3 feladat: Célba érkező női sportolók: {noiDarab} fő')

leghosszabbNevuFuto = eredmenyek[0]
for item in eredmenyek:
    if(item.nev) > len(leghosszabbNevuFuto.nev):
        leghosszabbNevuFuto = item
print('3.4 feladat: A leghosszabb női futó:')
print(f'\t Neve: {leghosszabbNevuFuto.nev}')

ferfiOsszIdo = 0
ferfiDarab = 0
for item in eredmenyek:
    if item.kategoria == 'Ferfi' and item.szazalek == 100:
        ferfiOsszIdo += item.idoOraban
