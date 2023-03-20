import PySimpleGUI as sg
import Databasen as dbs

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.


def makewindow(nummer):
    if nummer==0:
        layout = [
            [sg.Button("lägg till!"), sg.Button("ta bort"), sg.Button("sök")]
        ]
    elif nummer==1:
        layout = [
            [sg.Text('Förnamn'), sg.InputText()],
            [sg.Text('Efternamn'), sg.InputText()],
            [sg.Text('Gatuadress'), sg.InputText()],
            [sg.Text('postnummer'), sg.InputText()],
            [sg.Text('Postadress'), sg.InputText()],
            [sg.Text('Betallat'), sg.InputText()],
            [sg.Button('lägg till!')]
        ]
    elif nummer==2:
        layout = [
            [sg.Text("Id som ska tas bort:"), sg.InputText()],
            [sg.Button("ta bort")]
        ]
    elif nummer==3:
        layout = [
            [sg.Text("Id som ska sökas:"), sg.InputText()],
            [sg.Text(key="hej")],
            [sg.Button("sök")]
        ]

    return sg.Window("window", layout)

dbs.CreateDB()
dbs.Inserted("Sebbe", "Schaub","Sebbevägen 2", "Jajavägen", "11231", "False")
dbs.selectuser(1)
sak=0
grej=0


window=makewindow(0)

while grej==0:

    if sak==0:
        while sak==0:
            event, values = window.read()
            if event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
                grej=1
                break
            elif event == "lägg till!":
                sak=1
                win = makewindow(1)
                window.close()
                window2=win

            elif event == "ta bort":
                sak=2
                win = makewindow(2)
                window.close()
                window3 = win

            elif event == "sök":
                sak=3
                win = makewindow(3)
                window.close()
                window4 = win


    elif sak==1:    #lägg till event chane
        while sak==1:
            event2, values2 = window2.read()
            if event2 == sg.WIN_CLOSED:
                sak=0
                win = makewindow(0)
                window2.close()
                window = win
                break
            elif event2 == "lägg till!":
                dbs.Inserted(values2[0], values2[1], values2[2], values2[3], values2[4], values2[5])
                sak=1

    elif sak==2: #Ta bort event chane
        while sak==2:
            event3, values3 = window3.read()
            if event3 == sg.WIN_CLOSED:
                sak=0
                win = makewindow(0)
                window3.close()
                window = win
                break

            elif event3 == "ta bort":
                dbs.deleteuser(values3[0])
                sak=2

    elif sak==3: #sök event chane
        while sak==3:
            event4, values4 = window4.read()
            if event4 == sg.WIN_CLOSED:
                sak = 0
                win = makewindow(0)
                window4.close()
                window = win
                break

            elif event4 == "sök":
                window4["hej"].Update(dbs.selectuser(values4[0]))
                sak=3

window.close()