
                                #ska ta in en lista med temperaturer float samt vilken station till vilken temp
                                #sedan beräkna medelvärdet. sedan skriva ut alla temperaturer som är högre än medel
                                #samt vilken station som temperaturerna tillhör nr

s=input("Skriv ett antal temperaturer: (-1.2 4.7 22 22.2 18.2 -19) ")
temp_s=s.split()
ny_s=[float(b) for b in temp_s]
antal=0
a=0
print(ny_s)
ny_a=0
for a in ny_s:
    antal=antal+float(a)
    ny_a=ny_a+1
medel=antal/ny_a
a=0
antal=0
print(medel)
for a in ny_s:
    antal = antal + 1
    if float(a)>medel:
        print("temperaturen", float(a), "är större än medel, I station", antal)


