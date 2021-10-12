from tkinter import *
from captura_pachet import Capture
from diagrama_circulara import creare_diagrama_circulara

def start_proces():
    window =Tk()
    window.title('Captura completa.')
    window.geometry("400x250")
    Capture.get_instance()
    Capture.make_captura()
    Label(window, text = 'Captura completa!!', font=("Times New Roman", 15),
            bg="blue",fg="white",width=50,height=20).pack(side=BOTTOM)
    window.mainloop()


def verificare_filtru(entry):
    expresie = str(entry.get())
    lista_expresii = ['pachete', 'tcp', 'ip', 'udp', 'captura']
    while expresie not in lista_expresii:
        def afisare_mesaj_filtru():
            window = Tk()
            window.title('Filtru')
            window.geometry("400x250")
            Label(window, text='Filtru invalid!\nIncearca alt cuvant cheie!', font=("Times New Roman", 15),
                  bg="red", fg="black", width=50, height=20).pack(side=BOTTOM)
            window.mainloop()
        afisare_mesaj_filtru()
        break
    else:
        start_proces()


def open_pornire_captura():
    expresie = ''
    top = Toplevel()
    top.title('Pornire Captura')
    top.geometry("400x250")
    second_label = Label(top,text='Aplica filtru pentru pornire captura:')
    second_label.place(relx=0.5, rely=0.1, anchor=CENTER)
    second_entry = Entry(top, textvariable=expresie, width=20)
    second_entry.place(relx=0.5, rely=0.2, anchor=CENTER)
    Button(top, text = 'Submit', command = lambda: verificare_filtru(second_entry), bg='grey', width = 6).\
        place(relx=0.5, rely=0.3, anchor=CENTER)
    start_buton = Button(top, text='START', command = start_proces,bg='green',
                         width=15, font = ("Times New Roman", 12))
    start_buton.place(relx=0.5, rely=0.7, anchor=CENTER)
    #Label(top, text='Pornire captura:', width=20).pack(side = BOTTOM)

def open_show_statistics():
    if Capture.captura_pachete != None:
        creare_diagrama_circulara(Capture.nr_pachete_tcp, Capture.nr_pachete_udp)
    else:
        window = Tk()
        window.title('Eroare')
        window.geometry("300x150")
        Label(window, text='Fa o captura mai intai!', font=("Times New Roman", 15),
              bg="red", fg="black", width=50, height=20).place(relx=0.5, rely=0.5, anchor=CENTER)
        window.mainloop()

def press(entry):
    expresie = str(entry.get())
    Capture.save_json(expresie)
    def afisare_mesaj():
        window = Tk()
        window.title('Fisier')
        window.geometry("400x250")
        Label(window, text='Fisier salvat!', font=("Times New Roman", 15),
              bg="green", fg="yellow", width=50, height=20).pack(side=BOTTOM)
        window.mainloop()
    afisare_mesaj()


def open_save_as_json():
    if Capture.captura_pachete != None:
        expresie = ''
        second_top = Toplevel()
        second_top.title('Save as JSON:')
        second_top.geometry("400x250")
        Label(second_top, text='Introduceti calea pentru salvarea fisierului:'). \
            place(relx=0.5, rely=0.25, anchor=CENTER)
        entry_expresie = Entry(second_top, textvariable=expresie, bg='yellow')
        entry_expresie.place(relx=0.5, rely=0.4, anchor=CENTER)
        Button(second_top, text='Save', command=lambda: press(entry_expresie), bg='grey', width=6). \
            place(relx=0.5, rely=0.55, anchor=CENTER)
    else:
        window = Tk()
        window.title('Eroare')
        window.geometry("300x150")
        Label(window, text='Inainte de a salva,\n fa o captura mai intai!', font=("Times New Roman", 15),
              bg="red", fg="black", width=50, height=20).place(relx=0.5, rely=0.5, anchor=CENTER)
        window.mainloop()


def legenda():
    new_window = Toplevel()
    new_window.title('Legenda folosire butoane')
    new_window.geometry("550x200")
    Label(new_window, text='Legenda utilizare butoane:',font=("Times New Roman", 12))\
        .place(relx=0.1, rely=0.2, anchor=W)
    Label(new_window, text='Buton Pornire Captura - porneste program ce efectueaza o captura pe pachete')\
        .place(relx=0.1, rely=0.35, anchor=W)
    Label(new_window, text='Buton Save as Json - salveaza captura intr-un fisier de tip JSON') \
        .place(relx=0.1, rely=0.45, anchor=W)
    Label(new_window, text='Show statistics - creaza o diagrama circulara a pachetelor UDP si TCP.') \
        .place(relx=0.1, rely=0.55, anchor=W)