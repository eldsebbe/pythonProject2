
n=9.9999

while n>0:
    n=float(input("Säg en höjd! "))

    while n>0.01:
        print(n, "m")
        n=n*0.7
