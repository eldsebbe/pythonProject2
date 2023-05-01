

    #1 3 9 16 ...    koplingen är    k=1 k=k+2

n=int(input("Skriv ett sifra "))
summa=0
k=1

for k in range(k*k,n*n,2):
    summa = summa + k

print("Summan är", summa)