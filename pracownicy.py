class Pracownik:

    # def __init__(self,line):
    #     [self.surname, self.name, self.pesel, self.post, self.salary] = line.split(",")

    def __init__(self, surname, name, pesel, post, salary):

            self.surname = surname
            self.name = name
            self.pesel = pesel
            self.post = post
            self.salary = salary

    def __str__(self):

            s = "surname: " + self.surname + "\n"
            s += "name: " + self.name + "\n"
            s += "Pesel: " + str(self.pesel) + "\n"
            s += "post: " + self.post + "\n"
            s += "salary: " + str(self.salary) + "\n"

            return s


class Programista(Pracownik):

    def __init__(self,line):
        surname = line[0]
        name = line[1]
        pesel = line[2]
        post = line[3]
        salary = line[4]
        langs = line[5]

        if len(line) == 7:
            self.capab = line[6]
        else:
            self.capab = None

        super().__init__(surname, name, pesel, post, salary)
        self.langs = langs

    def __str__(self):

        langs = "temp"

        for lang in self.langs.split(" "):
            langs += "\n"
            langs += "- " + lang

        if self.capab is not None:
            s = super().__str__() + "\n"
            s += "Dodatkowe capab: " + self.capab
            s += "\nProgramista zna nastepujace langs: " + langs

            return s
        else:
            return super().__str__() + "\nProgramista zna nastepujace langs programowania: " + langs


class Sprzedawca(Pracownik):

    # def __init__(self, name,  pesel , surname, pensja, langs, charakter):
    #     Pracownik.__init__(name, surname,pesel,pensja)
    #     self.langs = langs
    #     self.charakter = charakter
    #
    # def __str__(self):
    #     s = Pracownik.__str__(self) + "\n"
    #     s += "Sprzedawca posluguje sie jezykami: " + self.langs + "\n"
    #     s += "Charakterystyka pracy: " + self.charakter +"\n"
    #
    #     return s

    def __init__(self, line):

        surname = line[0]
        name = line[1]
        pesel = line[2]
        post = line[3]
        salary = line[4]
        langs = line[5]
        char = line[6]

        if len(line) == 8:
            self.capab = line[7]
        else:
            self.capab = None

        super().__init__(surname, name, pesel, post, salary)
        self.langs = langs
        self.char = char

    def __str__(self):

        langs = "temp"

        for lang in self.langs.split(" "):
            langs += "\n- " + lang

        if self.capab is not None:
            s = super().__str__() + "\nDodatkowe capab: " + self.capab
            s += "\nSprzedawca posluguje sie nastepujacymi langami: " + langs
            s += "\nCharakterystyka pracy: " + self.char
            return s
        else:
            s = super().__str__() + "\nSprzedawca posluguje sie nastepujacymi langami: " + langs
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



