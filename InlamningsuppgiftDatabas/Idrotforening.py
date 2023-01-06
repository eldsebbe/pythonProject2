import PySimpleGUI as sg
import Databasen as dbs

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout1 = [
    [sg.Text('Förnamn'), sg.InputText()],
    [sg.Text('Efternamn'), sg.InputText()],
    [sg.Text('Gatuadress'), sg.InputText()],
    [sg.Text('postnummer'), sg.InputText()],
    [sg.Text('Postadress'), sg.InputText()],
    [sg.Text('Betallat'), sg.InputText()],
    [sg.Button('lägg till!')]
]
layout2 = [
    [sg.Button("lägg till!"), sg.Button("ta bort"), sg.Button("sök")]
]
layout3 = [
    [sg.Text("Id som ska tas bort:"), sg.InputText()],
    [sg.Button("ta bort")]
]
layout4 = [
    [sg.Text("Id som ska sökas:"), sg.InputText()],
    [sg.Button("sök")]
]

# Create the Window
window = sg.Window('Menu', layout2)
window2 = sg.Window('Lägg till', layout1)
window3= sg.Window("Ta bort", layout3)
window4= sg.Window("Sök", layout4)
# Event Loop to process "events" and get the "values" of the inputs

dbs.CreateDB()
dbs.Inserted("Sebbe", "Schaub","Sebbevägen 2", "Jajavägen", "11231", "False")
dbs.selectuser(1)
sak=0
grej=0

while grej==0:

    if sak==0:
        while sak==0:
            event, values = window.read()
            if event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
                grej=1
                break
            elif event == "lägg till!":
                print("Yes")
                #window.close()
                sak=1

            elif event == "ta bort":
                print("no")
                #window.close()
                sak=2

            elif event == "sök":
                print("maybe")
                #window.close()
                sak=3


    elif sak==1:    #lägg till event chane
        while sak==1:
            event2, values2 = window2.read()
            if event2 == sg.WIN_CLOSED:
                sak=0
                break
            elif event2 == "lägg till!":
                print('You entered ', values2[0], values2[1], values2[2], values2[3], values2[4], values2[5])
                dbs.Inserted(values2[0], values2[1], values2[2], values2[3], values2[4], values2[5])
                sak=1

    elif sak==2: #Ta bort event chane
        while sak==2:
            event3, values3 = window3.read()
            if event3 == sg.WIN_CLOSED:
                sak=0
                break

            elif event3 == "ta bort":
                print('You entered ', values3[0])
                dbs.deleteuser(values3[0])
                sak=2

    elif sak==3: #sök event chane
        while sak==3:
            event4, values4 = window4.read()
            if event4 == sg.WIN_CLOSED:
                sak = 0
                break

            elif event4 == "sök":
                print('You entered ', values4[0])
                print(dbs.selectuser(values4[0]))
                sak=3


print(dbs.selectuser(2))

window.close()