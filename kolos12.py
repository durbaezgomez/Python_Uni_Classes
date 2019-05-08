import datetime
import re


class Zwierze:
    def __init__(self,rasa, imie, wiek):
        self.rasa = rasa
        self.imie = imie
        self.wiek = wiek

    def __str__(self):
        s = "Rasa: " + self.rasa + "\n"
        s += "Imie: " + self.imie + "\n"
        s += "Wiek (w latach): " + str(self.wiek) + "\n"

        return s

    def obliczWiek(self):
        now = datetime.datetime.now()
        temp = now.year - self.wiek
        self.wiek = temp


class Kot(Zwierze):
    def __init__(self,rasa, imie, wiek, kolor1, kolor2, specjal1, specjal2):
        Zwierze.__init__(self,rasa, imie, wiek)
        self.kolor1 = kolor1
        self.kolor2 = kolor2
        self.specjal1 = specjal1
        self.specjal2 = specjal2

    def __str__(self):
        s = Zwierze.__str__(self) + "\n"
        s += "Kot ma nastepujace kolory: " + "\n" + "- "+ self.kolor1 + "\n"
        s += "- " + self.kolor2 + "\n"
        s += "Kot lubi nastepujace specjaly: " + "\n" + "- " + self.specjal1 + "\n"
        s += "- "+ self.specjal2 + "\n"

        return s


class Pies(Zwierze):
    def __init__(self,rasa, imie, wiek, siersc, glosnosc):
        Zwierze.__init__(self,rasa, imie, wiek)
        self.siersc = siersc
        self.glosnosc = glosnosc

    def __str__(self):
        s = Zwierze.__str__(self) + "\n"
        s += "Charakterystyka siersci: " + self.siersc + "\n"
        s += "Glosnosc szczekania: " + str(self.glosnosc) + "\n"

        return s

#
# class Pets:
#     def __init__(self, file_lines):
#         self.petsList = []
#         i=0
#         for line in file_lines:
#             self.petsList.append(Zwierze(line))
#             i += 1
#
#     def getPetsByString(self, str1, atrr):
#         for pet in self.carsList:
#             if getattr(pet,atrr) == str1:
#                 return pet
#         return None

#  MAIN

with open("zwierzeta.txt") as file:
    lines = file.read().splitlines()
file.close()

print (lines)

kot1 = Kot('Kot syjamski','Johnny',3,'szary','bialy','smieszny','drapie')
print (kot1)
