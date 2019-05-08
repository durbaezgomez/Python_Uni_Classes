from laby.produkty import PolskiProdukt;


class Samochod:
    def __init__(self, marka, rokProdukcji, liczbaDrzwi, przebieg="", kolor=""):
        self.marka = marka
        self.rokProdukcji = rokProdukcji
        self.przebieg = przebieg
        self.kolor = kolor
        self.liczbaDrzwi = liczbaDrzwi

    def __str__(self):
        s = "Marka = " + self.marka + "\n"
        s += "Rok produkcji = " + str(self.rokProdukcji) + "\n"
        s += "Przebieg = " + str(self.przebieg) + "\n"
        s += "kolor = " + self.kolor + "\n"
        s += "Liczba drzwi = " + str(self.liczbaDrzwi) + "\n"

        return s


class Maluch(Samochod, PolskiProdukt):
    czyJezdzi = True

    def __init__(self, miasto, firma, marka, rokProdukcji, glosnosc, przebieg, kolor):
        PolskiProdukt.__init__(self, miasto, firma)
        Samochod.__init__(self, marka, rokProdukcji, 2, przebieg, kolor)
        self.glosnosc = glosnosc

    def __str__(self):
        s = Samochod.__str__(self) + "\n"
        s += PolskiProdukt.__str__(self) + "\n"
        s += "Glosnosc: " + str(self.glosnosc) + "\n"
        s += "Czy jezdzi :" + str(self.czyJezdzi) + "\n"

        return s


class Porsche(Samochod):
    def __init__(self, marka, rokProdukcji, liczbaDrzwi, przebieg, kolor, ileDoSetki):
        Samochod.__init__(self, marka, rokProdukcji, liczbaDrzwi, przebieg, kolor)
        self.ileDoSetki = ileDoSetki

    def __str__(self):
        s = Samochod.__str__(self)
        s += "Ile do setki: " + str(self.ileDoSetki) + "\n"


        return s

