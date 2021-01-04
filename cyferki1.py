import tkinter as tk
from tkinter import ttk, BOTH
import random

licznik = 0
plus = 0
minus = 0
plus_napis = ""
minus_napis = ""
window = tk.Tk()
window.geometry("250x700")
window.title("Gierka")
label = tk.Label(window, text="Twoja Liczba")
label.grid(row=0, column=0)


def callback(sv):
    sv.set(sv.get()[:4])


sv = tk.StringVar()
sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))
entry = tk.Entry(window, width=8, textvariable=sv)

entry.grid(row=0, column=1)
entry.focus()

#akcja 1 to losowanie cyfer
def akcja1():
    global licznik
    licznik += 1
    global los
    los = [0, 0, 0, 0]
    # losowanie liczby 1
    los[0] = random.randint(0, 9)
    #print("los0 " + str(los[0]))

    # losowanie liczby 2
    los[1] = random.randint(0, 9)
    #print("los1 " + str(los[1]))
    while los[1] == los[0]:
        los[1] = random.randint(0, 9)
        #print("los1 nowe " + str(los[1]))

    # losowanie liczby 3
    los[2] = random.randint(0, 9)
    #print("los2 " + str(los[2]))
    while los[2] == los[1] or los[2] == los[0]:
        los[2] = random.randint(0, 9)
        #print("los2 nowe " + str(los[2]))

    # losowanie liczby 4
    los[3] = random.randint(0, 9)
    #print("los3 " + str(los[3]))
    while los[3] == los[1] or los[3] == los[0] or los[3] == los[2]:
        los[3] = random.randint(0, 9)
        #print("los3 nowe " + str(los[3]))

    #text = str(los[0]) + str(los[1]) + str(los[2]) + str(los[3])
    #label2 = tk.Label(window, text=text)
    #label2.grid(row=licznik, column=0)
    #print(los[0], los[1], los[2], los[3])

akcja1()


def akcja2(event=None): #event=none  zeby hotkey działał
    s = sv.get()
    if len(s) == 4:
        global plus
        global minus
        liczba = entry.get()
        global licznik
        licznik += 1
        #sprawdzanie cyfry 1
        if int(liczba[0]) == los[0]:
            plus +=1
            #print("+ 1 cyfra")
        elif int(liczba[0]) == los[1] or int(liczba[0]) == los[2] or int(liczba[0]) == los[3]:
            minus +=1
            #print("- 1 cyfra")

        #sprawdzanie cyfry 2
        if int(liczba[1]) == los[1]:
            plus +=1
            #print("+ 2 cyfra")
        elif int(liczba[1]) == los[0] or int(liczba[1]) == los[2] or int(liczba[1]) == los[3]:
            minus +=1
            #print("- 2 cyfra")

        # sprawdzanie cyfry 3
        if int(liczba[2]) == los[2]:
            plus += 1
            #print("+ 3 cyfra")
        elif int(liczba[2]) == los[0] or int(liczba[2]) == los[1] or int(liczba[2]) == los[3]:
            minus += 1
            #print("- 3 cyfra")

        # sprawdzanie cyfry 4
        if int(liczba[3]) == los[3]:
            plus += 1
            #print("+ 4 cyfra")
        elif int(liczba[3]) == los[0] or int(liczba[3]) == los[2] or int(liczba[3]) == los[1]:
            minus += 1
            #print("- 4 cyfra")

        if plus == 4:
            label2 = tk.Label(window, text="Wygrałes")
            label2.grid(row=licznik+1, column=0)
            entry.delete(0, "end")
            entry.insert(0, "")
            entry.configure(state=tk.DISABLED)
        #print(los[0], los[1], los[2], los[3])
        #print(liczba[0], liczba[1], liczba[2], liczba[3], "Moja liczba")

        text2 = liczba
        label2 = tk.Label(window, text=text2, font = ("Times New Roman", 15))
        label2.grid(row=licznik, column=1)

        label3 = tk.Label(window, text=licznik - 1)
        label3.grid(row=licznik, column=0)

        #dodawanie +
        for x in range(plus):
            global plus_napis
            plus_napis += "+"
        #print("plus_napisz: ", plus_napis)


        for x in range(minus):
            global minus_napis
            minus_napis += "-"
        #print("minus_napis: ", minus_napis)

        plus_minus = plus_napis + minus_napis

        label2 = tk.Label(window, text=plus_minus, font=("Courier", 8))
        label2.grid(row=licznik, column=2)
        minus_napis = ""
        plus_napis = ""
        #print("plus:", plus)
        #print("minus:", minus)
        #print("___________")
        plus = 0
        minus = 0
        entry.delete(0, "end")
        entry.insert(0, "")

button = tk.Button(window, text="ok", command=akcja2, width=13)
button.grid(row=0, column=2)



entry.bind('<Return>', akcja2)

window.mainloop()
