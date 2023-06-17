class CBadás:
    def __init__(self, sor:str) -> None:
        splitted = sor.split(';')

        self.Ora = int(splitted[0])
        self.Perc = int(splitted[1])
        self.AdasDb = int(splitted[2])
        self.Nev = splitted[3]