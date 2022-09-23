
                #en lista ska ta in ett antal heltal sedan skriva upp dem, sedan tar bort upprepande element

s=input("Skriv in ett antal heltal: (0 15 -7 -3 1) ")
temp_s=s.split()
a=0
nyny_s=[int(b) for b in temp_s]
for a in nyny_s:
    if nyny_s.count(int(a))>=2:
        while nyny_s.count(int(a))>=2:
            nyny_s.reverse()
            nyny_s.remove(int(a))
            nyny_s.reverse()


print("Utan upprepade heltal blir det: ", nyny_s)