class Pracownik:

    # def __init__(self,line):
    #     [self.nazwisko, self.imie, self.pesel, self.stanowisko, self.zarobki] = line.split(",")

    def __init__(self, nazwisko, imie, pesel, stanowisko, zarobki):
            self.nazwisko = nazwisko
            self.imie = imie
            self.pesel = pesel
            self.stanowisko = stanowisko
            self.zarobki = zarobki

    def __str__(self):
            s = "Nazwisko: " + self.nazwisko+ "\n"
            s += "Imie: " + self.imie+ "\n"
            s += "Pesel: " + str(self.pesel) + "\n"
            s += "Stanowisko: " + self.stanowisko + "\n"
            s += "Zarobki: " + str(self.zarobki) + "\n"

            return s


class Programista(Pracownik):

    def __init__(self,line):
        nazwisko = line[0]
        imie = line[1]
        pesel = line[2]
        stanowisko = line[3]
        zarobki = line[4]
        jezyki = line[5]
        if len(line) == 7:
            self.umiejetnosci = line[6]
        else:
            self.umiejetnosci = None

        super().__init__(nazwisko, imie, pesel, stanowisko, zarobki)
        self.jezyki = jezyki

    def __str__(self):
        jezyki = ""
        for jezyk in self.jezyki.split(" "):
            jezyki += "\n"
            jezyki += "- " + jezyk

        if self.umiejetnosci is not None:
            s = super().__str__() + "\n"
            s = "Dodatkowe umiejetnosci: " + self.umiejetnosci
            s += "\nProgramista zna nastepujace jezyki: " + jezyki

            return s
        else:
            return super().__str__() + "\nProgramista zna nastepujace jezyki programowania: " + jezyki


class Sprzedawca(Pracownik):
    # def __init__(self, imie,  pesel , nazwisko, pensja, jezyki, charakter):
    #     Pracownik.__init__(imie, nazwisko,pesel,pensja)
    #     self.jezyki = jezyki
    #     self.charakter = charakter
    #
    # def __str__(self):
    #     s = Pracownik.__str__(self) + "\n"
    #     s += "Sprzedawca posluguje sie jezykami: " + self.jezyki + "\n"
    #     s += "Charakterystyka pracy: " + self.charakter +"\n"
    #
    #     return s

    def __init__(self, line):
        nazwisko = line[0]
        imie = line[1]
        pesel = line[2]
        stanowisko = line[3]
        zarobki = line[4]
        jezyki = line[5]
        char = line[6]
        if len(line) == 8:
            self.umiejetnosci = line[7]
        else:
            self.umiejetnosci = None

        super().__init__(nazwisko, imie, pesel, stanowisko, zarobki)
        self.jezyki = jezyki
        self.char = char

    def __str__(self):
        jezyki = ""
        for jezyk in self.jezyki.split(" "):
            jezyki += "\n- " + jezyk
        if self.umiejetnosci is not None:
            s = super().__str__() + "\nDodatkowe umiejetnosci: " + self.umiejetnosci
            s += "\nSprzedawca posluguje sie nastepujacymi jezykami: " + jezyki
            s += "\nCharakterystyka pracy: " + self.char
            return s
        else:
            s = super().__str__() + "\nSprzedawca posluguje sie nastepujacymi jezykami: " + jezyki
            s += "\nCharakterystyka pracy: " + self.char
            return s


# class Pracownicy:
#     def __init__(self, linesList):
#         self.pracownikList=[]
#         for line in linesList:
#             self.pracownikList.append(Pracownik(line))

#  HARDCODE:
# pr1 = Programista('Nowy','Czarek',98823543,'Starszy programista','70000zl','Javascript')
# print (pr1)



