
t=float(input("temp? "))
if t<18:
    print("Det är kallt")
    print("sätt på värmen")
    if t<12 and t>-20:
        print("Sätt på jackan")
    else:
        print("Det är svinkallt")
else:
    print("Det är varmt")
    if t>=22 and t<40:
        print("Stäng av värmen")
    else:
        print("Det är svinvarmt")

print("Det är" , t ,"grader")