#maximall : L 600mm, T 100mm, bred+längd+tjocklek högst 900mm. Minimimått: L 140mm , bred 90mm

längd=int(input("hur långt är brevet (mm)"))
bredd=int(input("hur brett är brevet (mm)"))
tjock=int(input("hur tjockt är brevet (mm)"))

if längd>600 or längd<140 \
    or tjock>100 or bredd<90 \
    or längd+bredd+tjock>900:
    print("Det är fel i inmatningen dina måt är ej akseptavla!")

else:
    print("Du får posta brevet!")