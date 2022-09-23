

                                #gör om en mening till fikonspråk kaffe exempel kaffe= fiffe kakon


s=input("Skriv in ett ord: ")
a=0
s=s.lower()
temp_s="test"

for a in range(0,len(s),1):

    if s[a]=="a" or s[a]=="e" or s[a]=="i" or s[a]=="o" or s[a]=="u":
        temp_s= "fi"+s[a+1:] + " " + s[:a+1]+"kon"
        break

print(temp_s)