class Eredmeny:
    def __init__(self,sor:str) -> None:
        splitted =sor.split(';')
        self.nev = splitted[0]
        self.rajtszam = int(splitted[1])
        self.kategoria = splitted[2]
        self.ido = splitted[3]
        self.szazalek = int(splitted[4])

        splittedIdo = self.ido.split(':')
        self.idoOraban = int(splittedIdo[0]) + int(splittedIdo[1])/60 + int(splittedIdo[3])/3600