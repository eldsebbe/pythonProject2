

                            #lista i heltal(int) ska se hur många är mindre än 0

s=input("Skriv ett antal heltal: (0 15 -7 -3 1) ")
antal=0
ny_s=s.split()
a=0
for a in ny_s:

    if int(a)<0:
        antal = antal + 1



print("Det finns", antal, "negativa tal")