class Epulet:
    def __init__(self,row:str) -> None:
        splitted = row.split(';')
#név;város;ország;magasság;emelet;épült
        self.nev = splitted[0]
        self.varos = splitted[1]
        self.orszag = splitted[2]
        self.magassag = splitted[3]
        self.emelet = int(splitted[4])
        self.epult = splitted[5]

