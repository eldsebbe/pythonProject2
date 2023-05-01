class djur():

    def __init__(self, inx, iny, indx):
        self.x = inx
        self.y = iny
        self.distx = indx

    def nydistx(self,e):
        self.distx=e


def myFunc(e):
    return e.distx

ny=djur(106,0,0)
animals = []
animals.append(djur(111, 1, 0))
animals.append(djur(120, 2, 0))
animals.append(djur(90, 1, 0))             #ny x =106
animals.append(djur(105, 2, 0))
animals.append(djur(104, 2, 0))

for a in range(0,5):
    tempdisx=abs(animals[a].x-ny.x)
    animals[a].nydistx(tempdisx)


animals.sort(key=myFunc)
for i in range(0,5):
    print(animals[i].y ," ifrån: ",  animals[i].distx)
