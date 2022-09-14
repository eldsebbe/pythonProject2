

a=" Erik Andersson 990314-2714 "

a=a.strip()
i=a.rfind(" ")+1
j=a.find("-")
b=a[i:j]
b=b[4:] + "/" + b[2:4]
print(b)