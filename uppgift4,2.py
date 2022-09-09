

    #1 3 9 16 ...    koplingen är    k=1 k=k+2

n=int(input("Skriv ett sifra "))
summa=0
k=1

while k*k<=n*n:
    summa=summa+k
    k=k+2

print("Summan är", summa)