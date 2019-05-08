from laby import samochody


class AutoHandel:
    listaSamochodow = []

    def dodajSamochod(self, samochod):
        self.listaSamochodow.append(samochod)

    def usunSamochod(self, samochod):
        self.listaSamochodow.remove(samochod)

    def __str__(self):
        return "Autohandel ma samochody:" + samochod




samochod1 = samochody.Samochod('Lamborghini', 2012, 5)
samochod2 = samochody.Samochod('Bentley', 2016, 3, 15000, 'granatowy')
porsche = samochody.Porsche('Porsche', 2014, 3, 30000, 'grafitowe', 2.8)

maluch = samochody.Maluch("Warszawa", "BudPol", "Punto", 1999, 4, 20000, "zielony");

ah = AutoHandel()

ah.dodajSamochod(samochod1)
ah.dodajSamochod(samochod2)
ah.dodajSamochod(porsche)
ah.dodajSamochod(maluch)

for val in ah.listaSamochodow:
    print(val)

ah.usunSamochod(samochod1)
for val in ah.listaSamochodow:
    print(val)


