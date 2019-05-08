import pracownicy


with open("pracownicy.txt") as file:
    lines = file.read().splitlines()
file.close()

for line in lines:
    if "Programista" in line or "programista" in line:
        pracownik = pracownicy.Programista(line.split(','))
        print(pracownik.__str__() + "\n")
    if "sprzedaż" in line:
        pracownik = pracownicy.Sprzedawca(line.split(','))
        print(pracownik.__str__() + "\n")
