def zad1():

    num = 123
    list1 = []
    i = 0

    print "Dana jest liczba ", num

    while num > 0:
            list1.append = num%2;
            num = num/2
    list1.reverse()


    print(list1)

def zad1_2():

    num = 123
    list = [int(x) for x in bin(num)[2:]]

    print "dana jest liczba" , num
    print "utworzona lista: ", list

    x = bin(123)[2:]

    print num, " = ", x


def lotto():

    import random
    list1 = random.sample(range(1,49),5)
    print "Wylosowane liczby: ", list1

def zad3():

    dict1 = {
        "student1": {"nazwisko": "Kowalski", "imie": "Jan", "nr albumu": "12345"},
        "student2": {"nazwisko": "Adamski", "imie": "Adam", "nr albumu": "12346"},
        "student3": {"nazwisko": "Beacka", "imie": "Beata", "nr albumu": "12347"}
    }

    list1 = []
    for item in dict1.values():
        person = ""
        for val in item.values():
            person = person + " " + val

        list1.append(person)

    list1.sort()

    print list1

zad1_2()
print "\n"
lotto()
print "\n"
zad3()