import random
# import numpy


class Macierz():
    def __init__(self,n,m):
        self.n = n
        self.m = m

        self.arr = [[random.randint(1,2) for x in range(m)] for y in range(n)]

        # for item in range(self.n):
        #     self.arr.append([])
        #     for item2 in range(self.m):
        #         self.arr.append("")
        #
        # for item in range(self.n):
        #     self.arr.append([])
        #     for item2 in range(self.m):
        #         self.arr[item][item2] = random.randint(1,10)
        #         print(item, item2)

    def sumaWierszy(self):
        sumaW = 0
        for i in range(self.n):
            for j in range(self.m):
                sumaW += self.arr[i][j]

        return sumaW

    def sumaKolumn(self):
        sumaK = 0
        for i in range(self.m):
            for j in range(self.n):
                sumaK += self.arr[j][i]

        return sumaK

    def __str__(self):
        s = "Dana jest macierz losowa " + str(self.n) + " x " + str(self.m) + "\n"

        # s += str(self.arr)

        for item in range(self.n):
            for item2 in range(self.m):
                s += ('{:5d}'.format(self.arr[item][item2]))
            s += "\n\n"

        s += "Suma w kolumnach: " + str(a.sumaKolumn()) + "\n"
        s += "Suma w wierszach: " + str(a.sumaWierszy()) + "\n"
        return s






class MacierzTrojkatna(Macierz):
    def __init__(self, n, wlasciwosc = "L"):
        Macierz.__init__(self,n,m=None)
        self.wlasciwosc = wlasciwosc

        # if wlasciwosc == "U":
        #     for item in range(self.n)

    def __str__(self):

        s = "Dana jest macierz losowa trojkatna " + str(self.n) + " x " + str(self.n) + "\n"

        if self.wlasciwosc == "U":
            s += "\nJest to macierz trojkatna gorna"
        else:
            s += "\nJest to macierz trojkatna dolna"

        return s

a = Macierz(3, 5)
print(a)

