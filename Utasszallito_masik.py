from Repulo import *
from math import *

repulok : list[Repulo] = []

file = open('utasszallitok.txt', 'r', encoding='utf-8')
file.readline()
for sor in file:
    repulok.append(Repulo(sor.strip()))
file.close() 

print(f'4. feladat: Adatsorok száma: {len(repulok)}')

boeingDarab = 0
for item in repulok:
    if 'Boeing' in item.tipus:
        boeingDarab += 1
print(f'5. feladat: Boeing típusok száma: {boeingDarab}')

legtobbUtas = repulok[0]
for item in repulok:
    if item.utasSzam > legtobbUtas.utasSzam:
        legtobbUtas = item
print(f'6. feladat: A legtöbb utast szállító repülőgéptípus')
print(f'\tTipus: {legtobbUtas.tipus}')
print(f'\tÉv: {legtobbUtas.ev}')
print(f'\tUtas: {legtobbUtas.utas}')
print(f'\tSzemélyzet: {legtobbUtas.szemelyzet}')
print(f'\tUtazósebesség: {legtobbUtas.utazosebesseg}')

file = open('utasszallitok.txt', 'w', encoding='utf-8')
file.write('típus;év;utas;személyzet;utazósebesség;felszállótömeg;fesztáv\n')
for item in repulok:
    file.write(f'{item.tipus};{item.ev};{item.utas};{item.szemelyzet};{item.utazosebesseg};{round(item.felszallotomeg/1000)};{round(item.fesztav*3.2808)}\n')
file.close()


stat= {}
for item in repulok:
    if item.ev in stat.keys():
        stat[item.ev] += 1
else:
    stat[item.ev] = 1


print('Statisztika')
#print(stat)
for key, value in stat.items():
    print(f'\t{key}: {value} darab')


#Mach-kaékulator
torlonyomas = float(input('Torlónyomás: '))


mach = sqrt()