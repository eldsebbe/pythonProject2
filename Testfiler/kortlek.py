import random

class kort:
    def __init__(self, färg, nummer):
        self.tempfarg = färg
        self.nummer = nummer
        self.färg = "ovald"
        if self.tempfarg== 0:
            self.färg = "Spader"
        elif self.tempfarg== 1:
            self.färg = "Klöver"
        elif self.tempfarg== 2:
            self.färg = "Hjärter"
        else:
            self.färg = "Ruter"
    def visanummer(self):
        return self.nummer
    def visafärg(self):
        return self.färg
    def Skrivut(self):
        return self.färg, self.nummer


class kortlek:
    def __init__(self):
        self.Lek = []
        for h in range(0, 4):
            for i in range(1, 14):
                self.Lek.append(kort(h, i))
    def draettkort(self):
        self.temp_rand = random.randint(0, 52)
        return self.Lek[self.temp_rand].Skrivut()


sak = kortlek()
print(sak.draettkort())
