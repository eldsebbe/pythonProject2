def print_hi(name):
    print(f'Hi, {name}')
value_int= 10
value_strin="Python"
value_float= 12.43


print("Är nummeret negativt? Det ska vi tetsta")
b=0

while b==0:
    print("Skriv ett nummer")
    a=float(input())

    if a>=0:
        print("posetivt")
    else:
        print("Negativt")

    print("Vill du testa ett nytt nummer? ja/nej")
    skrivet_yes=input()

    if skrivet_yes=="nej" or skrivet_yes=="Nej":
        b=1
    else:
        b=0




print("Jag är fri")

