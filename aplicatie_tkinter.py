from tkinter import *
from PIL import ImageTk, Image
from functii_ajutatoare import start_proces, verificare_filtru, open_pornire_captura, \
    open_show_statistics, press, open_save_as_json, legenda

root_window = Tk()
root_window.title("Aplicatie captura pe interfetele de retea")
#root_window.geometry('400x250')
canvas = Canvas(root_window, width=500,height=350)
imagine = ImageTk.PhotoImage(Image.open('background.PNG'))

canvas.create_image(-20,0, anchor=NW, image=imagine)

canvas.pack()

Label(root_window, text='Captura Pachete', font=("Times New Roman", 14),
              bg="purple", fg="white").place(relx=0.72, rely=0.05, anchor=W)

pornire_captura = Button(root_window,
                         text = "Pornire Captura",
                         command=open_pornire_captura,
                         font = ("Times New Roman", 14),
                         bg = "Blue",
                         fg = "white",
                         width = 15,
                         height = 1)

pornire_captura.place(relx=0.53, rely=0.88, anchor=CENTER)

save_as_json = Button(text = "Save as JSON",
                      command = open_save_as_json,
                      font = ("Times New Roman", 12),
                      bg = "yellow",
                      fg = "black",
                      width = 10,
                      height = 1)

save_as_json.place(relx=0.75, rely=0.35, anchor=W)

show_statistics = Button(text = "Show statistics",
                         command = lambda:open_show_statistics(),
                         font = ("Times New Roman", 12),
                         bg = "Green",
                         fg = "white",
                         width = 10,
                         height = 1)
show_statistics.place(relx=0.75, rely=0.55, anchor=W)

legenda_butoane = Button(text = "Legenda",
                         command = lambda:legenda(),
                         font = ("Times New Roman", 10),
                         bg = "Brown",
                         fg = "white",
                         width = 10,
                         height = 1)
legenda_butoane.place(relx=0.2, rely=0.9, anchor=E)

close_program = Button(text = "Close",
                       command = lambda:exit(),
                         font = ("Times New Roman", 10),
                         bg = "red",
                         fg = "black",
                         width = 10,
                         height = 1)
close_program.place(relx=0.79, rely=0.9, anchor=W)

root_window.mainloop()

