from laby import funkcje
import math

class ZlaPodstawa(Exception):
    def __str__(self):
        return "Podana podstawa jest niepoprawna"


class ZlyArgument(Exception):
    def __str__(self):
        return "Podany argument jest niepoprawny!"


class RoznePodstawy(Exception):
    def __str__(self):
        return "Podane podstawy sa rozne!"


class Logarytm:

    def __init__(self, podstawa, argument):

        self.podstawa = podstawa
        self.argument = argument

    def __add__(self, log):

        argTemp = self.argument * log.argument
        wynik = "log" + str(self.podstawa) + "(" + str(argTemp) + ")" + "\n"

        if self.podstawa <=1:
            raise ZlaPodstawa()
        elif argTemp <= 0:
            raise ZlyArgument()
        elif self.podstawa != log.podstawa:
            raise RoznePodstawy()
        else:
            return wynik

    def redukuj(self):
        if type(self.podstawa) == int:
            x = funkcje.liczbaIWykladnik(funkcje.czynnikiPierwsze(self.podstawa))
            print(x)
            self.podstawa = x[0]

            self.argument = self.argument ** (1 / x[1])
            # return self
        else:
            raise TypeError()


    def oblicz(self):
        return math.log(self.argument,self.podstawa)


    def __str__(self):
        s = "log" + str(self.podstawa) + "(" + str(self.argument) + ")"
        return s
try:

    l1 = Logarytm(9,16)
    l2 = Logarytm(3,5)
    # l3 = l1 + l2

    # print (str(l1) + " + " + str(l2) + " = " + str(l3))

    print (l1.oblicz())

    # print (funkcje.czynnikiPierwsze(l1.argument))
    # print (funkcje.liczbaIWykladnik())

    l1.redukuj()
    print (l1)

except ZlaPodstawa as zlaP:
    print(zlaP)
except ZlyArgument as zlyA:
    print(zlyA)
except RoznePodstawy as rP:
    print(rP)
