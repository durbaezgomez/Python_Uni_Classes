class PolskiProdukt:

    def __init__(self, miasto, firma):
        self.miasto = miasto
        self.firma = firma

    def __str__(self):
        s = "Polskie auto!" + "\n"
        s += "z miasta: " + self.miasto +"\n"
        s += "z firmy: " + self.firma

        return s