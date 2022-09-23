

                                #Ska ta in mailadress och se till att den är giltig (förnamn.efternamn@mail.com)

s=input("Skriv in en giltig mail: (förnamn.efternamn@mail.com)")
if s.count(".")!=2 and s.count("@")!=1:
    print("Fel")
else:
    print("rätt")
    fnamn = s[:s.find(".")]
    enamn = s[s.find(".") + 1:s.find("@")]
    mail = s[s.find("@") + 1:s.rfind(".")]
    domain = s[s.rfind(".") + 1:]

print(s)
print(fnamn)
print(enamn)
print(mail)
print(domain)