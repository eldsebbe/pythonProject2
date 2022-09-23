
            #text string

print("Här ska vi testa om ett ord börjar och slutar med samma tecken.")
txt = input("Skriv ett ord")

if txt[0]==txt[len(txt)-1]:
    print("Det är samma!")
else:
    print("Fel!")