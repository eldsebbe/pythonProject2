
            #jämnför betygg. E=25, D=30, C=35, B=40, A=45
            #Max poäng är 50

elevens_poäng=0


elevens_poäng=int(input("Hur många poäng har eleven? "))


if elevens_poäng <=50 and elevens_poäng >=45:
    print("A")

elif elevens_poäng<45 and elevens_poäng>=40:
    print("B")
elif elevens_poäng<40 and elevens_poäng>=35:
    print("C")
elif elevens_poäng<35 and elevens_poäng>=30:
    print("D")
elif elevens_poäng<30 and elevens_poäng>=25:
    print("E")
elif elevens_poäng<25:
    print("Du har fått ett F snyggt jobbat")

else:
    print("Du har fått ett S")