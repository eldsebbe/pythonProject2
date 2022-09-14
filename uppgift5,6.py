            #svensk datum åååå/mm/dd  mm/dd/yyyy

print("I detta program ska vi översätta ett svenskt datum till ett americanskt datum")

datum=input("Skriv in ett datum (ååååmmdd)")
år=datum[:4]
månad=datum[4:6]
dag=datum[6:]


nydatum=månad + "/" + dag + "/" + år
print(nydatum)