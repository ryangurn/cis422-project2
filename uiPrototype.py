from tkinter import *
from tkinter.ttk import Notebook,Entry

# Creates Window
window = Tk()

# Creates the title you want to have on the window
window.title("RegTools")

# Specifies window size
window.geometry("600x400")
window.configure(background="#003011")

'''
la = Label(window, text="Mason")
la.grid(row=0, column=0)

la = Label(window, text="Alex")
la.grid(row=1, column=1)

la = Label(window, text="Woodenlegs")
la.grid(row=2, column=2)

la = Label(window, text="Logan")
la.grid(row=3, column=3)
'''

listBx1 = Listbox(window, background="#C9FFB7", selectbackground="Yellow", fg="Green")
listBx1.place(x=85,y=160, height=180, width=100)

listBx1.insert(0, "CIS 313")
listBx1.insert(0, "ENG 380")
listBx1.insert(0, "PHIL 230")



listBx2 = Listbox(window, background="White", selectbackground="Yellow", fg="#4A4A4A")
listBx2.place(x=195,y=160, height=180, width=100)

listBx2.insert(0, "CIS 315")
listBx2.insert(0, "CIS 330")
listBx2.insert(0, "CIS 422")
listBx2.insert(0, "MATH 341")




listBx3 = Listbox(window, background="#D3D3D3", selectbackground="Yellow", fg="#4A4A4A")
listBx3.place(x=305,y=160, height=180, width=100)

listBx3.insert(0, "CIS 415")
listBx3.insert(0, "CIS 407")
listBx3.insert(0, "HIST 122")
listBx3.insert(0, "ART 270")




listBx4 = Listbox(window, background="#D3D3D3", selectbackground="Yellow", fg="#4A4A4A")
listBx4.place(x=415,y=160, height=180, width=100)

listBx4.insert(0, "CIS 425")
listBx4.insert(0, "MATH 253")
listBx4.insert(0, "MATH 254")
listBx4.insert(0, "PHIL 310")


buttonLeft=Button(window,text="Prev")
buttonLeft.place(x=20,y=240, height=40, width=40)

buttonRight=Button(window,text="Next")
buttonRight.place(x=540,y=240, height=40, width=40)


# NEXT: FALL -> WINTER
# PREV: FALL -> SUMMER
label1=Label(window, text="FALL", background="#003011", fg="white")
label1.place(x=105,y=100, height=30, width=60)

# NEXT: 2019 -> 2020
# PREV: 2019 -> 2019
label1=Label(window, text="2019", background="#003011", fg="white")
label1.place(x=105,y=120, height=30, width=60)
label1a=Label(window, text="COMPLETE", background="#003011", fg="Green")
label1a.config(font=("Helvetica", 12))
label1a.place(x=95,y=340, height=30, width=80)

label2=Label(window, text="WINTER", background="#003011", fg="white")
label2.place(x=215,y=100, height=30, width=60)
label2=Label(window, text="2020", background="#003011", fg="white")
label2.place(x=215,y=120, height=30, width=60)
label2a=Label(window, text="IN PROGRESS", background="#003011", fg="white")
label2a.config(font=("Helvetica", 12))
label2a.place(x=205,y=340, height=30, width=80)

label3=Label(window, text="SPRING", background="#003011", fg="white")
label3.place(x=325,y=100, height=30, width=60)
label3=Label(window, text="2020", background="#003011", fg="white")
label3.place(x=325,y=120, height=30, width=60)
label3a=Label(window, text="N/A", background="#003011", fg="white")
label3a.config(font=("Helvetica", 12))
label3a.place(x=315,y=340, height=30, width=80)

label4=Label(window, text="SUMMER", background="#003011", fg="white")
label4.place(x=435,y=100, height=30, width=60)
label4=Label(window, text="2020", background="#003011", fg="white")
label4.place(x=435,y=120, height=30, width=60)
label4a=Label(window, text="N/A", background="#003011", fg="white")
label4a.config(font=("Helvetica", 12))
label4a.place(x=425,y=340, height=30, width=80)




# Keep window open
window.mainloop()
