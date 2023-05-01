def print_hi(name):
    print(f'Hi, {name}')

        #årskort biljett - val      årskort=2310    biljett=85
        #Ska jämnföra priser under en tid
        #se hur länge du ska stanna
kostnad=0
tid=0


val=int(input("årskort=2310kr, biljett=85kr, Vad vill du köpa? skriv (1) om årskort, skriv (2) om enkelbiljet. "))

if val==1:
    kostnad=2310
elif val==2:
    kostnad=85
else:
    print("du har gjort fel!")
    kostnad=9999999999


tid=int(input("Hur många dagar tänker du gymma? "))

if kostnad==2310:

    if kostnad>= 85*tid:
        print("Du borde köpt enkelbiljeter istället. Du slösar pengar")
    else:
        print("Du har gjort ett ekonomist korrekt val")
elif kostnad==85:
    if 2310 <= kostnad * tid:
        print("Du borde köpt årskort istället. Du slösar pengar")
    else:
        print("Du har gjort ett ekonomist korrekt val")

else:
    print("Mer Fel!")

print("Jag är fri")