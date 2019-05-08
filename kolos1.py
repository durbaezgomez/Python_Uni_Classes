import datetime
import re


class Zwierze:
    def __init__(self,line):
        [self.rasa, self.imie, self.wiek] = line.split(",")

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
    def __init__(self,line):
        Zwierze.__init__(self,line)
        [self.kolor1, self.kolor2, self.specjal1, self.specjal2] = line.split(",")

    def __str__(self):
        s = Zwierze.__str__(self) + "\n"
        s += "Kot ma nastepujace kolory: " + "\n" + "- "+ self.kolor1 + "\n"
        s += "- " + self.kolor2 + "\n"
        s += "Kot lubi nastepujace specjaly: " + "\n" + "- " + self.specjal1 + "\n"
        s += "- "+ self.specjal2 + "\n"

        return s


class Pies(Zwierze):
    def __init__(self, line):
        Zwierze.__init__(self, line)
        [self.siersc, self.glosnosc] = line.split(",")

    def __str__(self):
        s = Zwierze.__str__(self) + "\n"
        s += "Charakterystyka siersci: " + self.siersc + "\n"
        s += "Glosnosc szczekania: " + str(self.glosnosc) + "\n"

        return s


class Pets:
    def __init__(self, file_lines):
        self.petsList = []
        i=0
        for line in file_lines:
            self.petsList.append(Zwierze(line))
            i += 1

    def getPetsByString(self, str1, atrr):
        for pet in self.carsList:
            if getattr(pet,atrr) == str1:
                return pet
        return None

#  MAIN

with open("zwierzeta.txt") as file:
    lines = file.read().splitlines()
file.close()

lines = tuple(open('zwierzeta.txt', 'r'))
# print (lines)

# zw1 = Kot(lines[1])
# print (zw1)


# for l in lines:
#     zw1 = Zwierze(lines[l])
#     print (zw1)

lines = lines[1:]
pets = Zwierze(lines)

i = 0
for pets in pets.petsList:


    # wszystkie koty
    matchObj = re.match(r'(Kot) (.*?), (.*?),[0-9](.*),(.*?) (.*?) (.*?),(.*?) (.*?),(.*?)$', pets,re.M|re.I)
    print (matchObj)

