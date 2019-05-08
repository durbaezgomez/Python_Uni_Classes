import re


class Car:
    def __init__(self, line):
        [self.model, self.mpg, self.cylinders, self.disp, self.hp, self.weight, self.accelerate, self.year, self.origin] = line.split(",")

    def __str__(self):
        return self.model + " " + self.mpg + " " + self.cylinders + " " + self.disp + " " + self.hp + " " + self.weight + " " + self.accelerate + " " + self.year + " " + self.origin


class Cars:
    def __init__(self, file_lines):
        self.carsList = []
        i=0
        for line in file_lines:
            self.carsList.append(Car(line))
            i += 1

    def getCarsByString(self, str1, atrr):
        for car in self.carsList:
            if getattr(car,atrr) == str1:
                return car
        return None


with open("cars.csv") as file:
    lines = file.read().splitlines()
file.close()

lines = lines[1:]
cars = Cars(lines)

i = 0
for car in cars.carsList:

    # wszystkie samochody ford
    a = re.match(r'^(ford)(.*)$', getattr(car, 'model'))

    # wszystkie toyoty i volvo
    # a = re.match(r'^((toyota)|(volvo))(.*)$', getattr(car, 'model'))

    # wszystkie samochody majace liczbe w nazwie modelu
    # a = re.match(r'^(.*)[0-9](.*)$', getattr(car, 'model'))

    # wszystkie samochody majace nawias otwierajacy i zamykajacy w nazwie modelu
    # a = re.match(r'^(.*)\((.*)\)(.*)$', getattr(car, 'model'))

    # wszystkie samochody majace w nazwie chociaz jeden znak nie bedacy litera, cyfra lub spacja
    # a = re.match(r'^(.*)[^a-zA-Z\d\s](.*)$', getattr(car, 'model'))

    # wszystkie samochody majace w nazwie modelu dokladnie dwie spacje
    # a = re.match(r'^[^ ]* [^ ]* [^ ]*$', getattr(car, 'model'))

    # wszystkie samochody ktore w pierwszym slowie nazwy modelu maja dokladnie dwie samogloski
    # a = re.match(r'^[^aeiouy ]*[aeiouy][^aeiouy ]*[aeiouy][^aeiouy ]* +.*$', getattr(car, 'model'))

    # wszystkie samochody o dwucyfrowej liczbie koni mechanicznych
    # a = re.match(r'^[1-9][0-9]$', getattr(car, 'hp'))

    # wszystkie samochody ktorych przyspieszenie jest liczba z kropka
    # a = re.match(r'^[0-9]+\.[0-9]+$', getattr(car, 'accelerate'))

    # wszystkie samochody ktorych rok produkcji to lata siedemdziesiate
    # a = re.match(r'^7[0-9]$', getattr(car, 'year'))

    if a:
        print(a.group())
        i += 1

print("\n\nZnaleziono " ,(i), " samochodow")