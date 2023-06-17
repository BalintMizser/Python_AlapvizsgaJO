from Epulet import *

epuletek:list[Epulet] = []
file = open('legmagasabb.txt', 'r', encoding='utf-8')
file.readline()
for row in file:
    epuletek.append(Epulet(row.strip()))
file.close()

print(f'3.2 feladat: Épületek száma: {len(epuletek)} db')

sum = 0
for item in epuletek:
    sum += item.emelet
print(f'3.3 feladat: Emeletek összege: {sum}')

print('A legmagasabb épület adatai')
maxEpulet = epuletek[0]
for item in epuletek:
    if item.magassag > maxEpulet.magassag:
       maxEpulet = item
print(f'\tNév: {maxEpulet.nev}')
print(f'\tVáros: {maxEpulet.varos}')
print(f'\tOrszág: {maxEpulet.orszag}')
print(f'\tMagasság: {maxEpulet.magassag}')
print(f'\tEmeletek száma: {maxEpulet.emelet}')
print(f'\tÉpítés éve: {maxEpulet.epult}')

for item in epuletek:
    if item.orszag == 'Olaszország':
        print('3.5 feladat: Van olasz épület az adatok között')
        break
