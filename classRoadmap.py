from tkinter import *
from tkinter.ttk import Notebook,Entry

idx = 0

def box1_update():
# Updates listbox 1 with class data given the key
	global listBx1
	for i in range(len(classMap[classMapKeys[idx]])):
		listBx1.insert(0, classMap[classMapKeys[idx]][i])


def box2_update():
# Updates listbox 2 with class data given the key
	global listBx2
	for i in range(len(classMap[classMapKeys[idx+1]])):
		listBx2.insert(0, classMap[classMapKeys[idx+1]][i])


def box3_update():
# Updates listbox 3 with class data given the key
	global listBx3
	for i in range(len(classMap[classMapKeys[2]])):
		listBx3.insert(0, classMap[classMapKeys[idx+2]][i])


def box4_update():
# Updates listbox 4 with class data given the key
	global listBx4
	for i in range(len(classMap[classMapKeys[idx+3]])):
		listBx4.insert(0, classMap[classMapKeys[idx+3]][i])


def update_next(event):
# Function for the "Next" button
	global idx
	# Checks to see if end has been reached
	if(idx >= (len(classMap)-4)):
		return
	else:
		# Sets button to green
		buttonPrev.config(background="#369148", fg="#e6e6e6")
		
		if((idx >= len(classMap)-5)):
			# Sets button to grey
			buttonNext.config(background="#808080", fg="#e6e6e6")

		idx += 1
		# Erases listboxes
		listBx1.delete(0, END)
		listBx2.delete(0, END)
		listBx3.delete(0, END)
		listBx4.delete(0, END)

		# Updates listboxes
		box1_update()
		box2_update()
		box3_update()
		box4_update()

		# Modifies the listbox text titles with quarter info
		global classMapKeys
		label1['text'] = classMapKeys[idx]
		label2['text'] = classMapKeys[idx+1]
		label3['text'] = classMapKeys[idx+2]
		label4['text'] = classMapKeys[idx+3]


def update_prev(event):
# Function for the "Prev" button
	global idx
	# Checks to see if beginning has been reached
	if(idx == 0):
		return
	else:
		# Sets button to green
		buttonNext.config(background="#369148", fg="#e6e6e6")

		if(idx-1 == 0):
			# Sets button to grey
			buttonPrev.config(background="#808080", fg="#e6e6e6")

		idx -= 1
		# Erases listboxes
		listBx1.delete(0, END)
		listBx2.delete(0, END)
		listBx3.delete(0, END)
		listBx4.delete(0, END)

		# Updates listboxes
		box1_update()
		box2_update()
		box3_update()
		box4_update()

		# Modifies the listbox text titles with quarter info
		global classMapKeys
		label1['text'] = classMapKeys[idx]
		label2['text'] = classMapKeys[idx+1]
		label3['text'] = classMapKeys[idx+2]
		label4['text'] = classMapKeys[idx+3]

def backToClassMenu(event):
	# Function to go back to the classes menu
	print("Goes back to class menu")

# Empty list that will store the class keys in same order as dictionary
classMapKeys = []

# Dummy class data I made
classMap = {
"Spring 2019":["CIS 210", "SOC/SCI (4 Cr)", "ARTS/LETTER (4 Cr)", "MATH 241"],
"Summer 2019":["CIS 211", "MATH 242", "ARTS/LETTER (4 Cr)"],
"Fall 2019":["CIS 212", "ENG 380", "ARTS/LETTER (4 Cr)"],
"Winter 2020":["CIS 315","CIS 330","CIS 422","MATH 341"],
"Spring 2020":["CIS 415","CIS 407","HIST 122","ARTS/LETTER (4 Cr)"],
"Summer 2020":["CIS 425","MATH 253","MATH 254","PHIL 310"],
"Fall 2020":["MATH 433", "SOC/SCI (4 Cr)", "SOC/SCI (4 Cr)", "MATH 488"],
"Winter 2021":["CIS 443", "MATH 343", "SOCIAL SCIENCE (4 Cr)", "SOCIAL SCIENCE (4 Cr)"]
}

# Populates a list of keys (in order) from the classMap data
for i in range(len(classMap)):
	classMapKeys.append([key for key in classMap.keys()][i])

# Creates Window
window = Tk()

# Creates the title you want to have on the window
window.title("RegTools")

# Specifies window size
window.geometry("800x600+120+120")
window.configure(background="#323232")

# Lower (dark) half of the window
labelNext=Label(window, text="", background="#282929", fg="#e6e6e6")
labelNext.place(x=0,y=125, height=475, width=800)

# Green Stripe
labelNext=Label(window, text="", background="#369148", fg="#e6e6e6")
labelNext.place(x=0,y=122, height=8, width=800)

# RoadMap Text
roadMapLabel = Label(window, text="ROADMAP", background="#323232", fg="#ffcc00")
roadMapLabel.place(x=-150,y=5, height=115, width=600)
roadMapLabel.config(font=("Helvetica", 37))

# UO Logo
image = PhotoImage(file="UOicon.gif")
label = Label(image = image)
label.place(x=670,y=5)
l1 = Label(window, text="", background="#323232", fg="#e6e6e6")
l1.place(x=670,y=5, height=5, width=140)
l2 = Label(window, text="", background="#323232", fg="#e6e6e6")
l2.place(x=790,y=5, height=115, width=5)
l3 = Label(window, text="", background="#323232", fg="#e6e6e6")
l3.place(x=670,y=5, height=115, width=5)
l4 = Label(window, text="", background="#323232", fg="#e6e6e6")
l4.place(x=670,y=117, height=5, width=130)

# Initializes listboxes 1
listBx1 = Listbox(window, background="#323232", selectbackground="#369148", fg="#e6e6e6")
listBx1.place(x=60,y=195, height=285, width=155)

# Initializes listboxes 2
listBx2 = Listbox(window, background="#323232", selectbackground="#369148", fg="#e6e6e6")
listBx2.place(x=235,y=195, height=285, width=155)

# Initializes listboxes 3
listBx3 = Listbox(window, background="#323232", selectbackground="#369148", fg="#e6e6e6")
listBx3.place(x=410,y=195, height=285, width=155)

# Initializes listboxes 4
listBx4 = Listbox(window, background="#323232", selectbackground="#369148", fg="#e6e6e6")
listBx4.place(x=585,y=195, height=285, width=155)

# Populates all the listboxes
box1_update()
box2_update()
box3_update()
box4_update()

# "Next" Button
labelNext=Label(window, text="NEXT", background="#282929", fg="#e6e6e6")
labelNext.config(font=("Arial", 12))
labelNext.place(x=750,y=280, height=20, width=40)

# "Prev" Button
labelPrev=Label(window, text="PREV", background="#282929", fg="#e6e6e6")
labelPrev.config(font=("Arial", 12))
labelPrev.place(x=10,y=280, height=20, width=40)

# if the data doesn't have at least 4 quarters of data, grey out "Next" button
if(len(classMapKeys) <= 4):
	buttonNext=Label(window, text=">", background="#808080", fg="#e6e6e6")
	buttonNext.config(font=("Arial Bold", 22))
	buttonNext.place(x=750,y=300, height=40, width=40)
	buttonNext.bind("<Button-1>", update_next)
else:
	# Set to green if it doesn't
	buttonNext=Label(window, text=">", background="#369148", fg="#e6e6e6")
	buttonNext.config(font=("Arial Bold", 22))
	buttonNext.place(x=750,y=300, height=40, width=40)
	buttonNext.bind("<Button-1>", update_next)

# If the index is 0, grey out the "Prev" button
if(idx == 0):
	buttonPrev=Label(window, text="<", background="#808080", fg="#e6e6e6")
	buttonPrev.config(font=("Arial Bold", 22))
	buttonPrev.place(x=10,y=300, height=40, width=40)
	buttonPrev.bind("<Button-1>", update_prev)
else:
	# Set to green if it doesn't
	buttonPrev=Label(window, text="<", background="#369148", fg="#e6e6e6")
	buttonPrev.config(font=("Arial Bold", 22))
	buttonPrev.place(x=10,y=300, height=40, width=40)
	buttonPrev.bind("<Button-1>", update_prev)


# Title the titles for each listbox 1
label1=Label(window, text=classMapKeys[idx], background="#282929", fg="#e6e6e6")
label1.config(font=("Arial Bold", 16))
label1.place(x=60,y=160, height=30, width=155)

# Optional text to be implemented for listbox 1
label1a=Label(window, text="", background="#282929", fg="Green")
label1a.config(font=("Helvetica", 16))
label1a.place(x=60,y=480, height=30, width=155)

# Title the titles for each listbox 2
label2=Label(window, text=classMapKeys[idx+1], background="#282929", fg="#e6e6e6")
label2.config(font=("Arial Bold", 16))
label2.place(x=235,y=160, height=30, width=155)

# Optional text to be implemented for listbox 1
label2a=Label(window, text="", background="#282929", fg="#e6e6e6")
label2a.config(font=("Helvetica", 16))
label2a.place(x=235,y=480, height=30, width=155)

# Title for each listbox 3
label3=Label(window, text=classMapKeys[idx+2], background="#282929", fg="#e6e6e6")
label3.config(font=("Arial Bold", 16))
label3.place(x=410,y=160, height=30, width=155)

# Optional text to be implemented for listbox 1
label3a=Label(window, text="", background="#282929", fg="white")
label3a.config(font=("Helvetica", 16))
label3a.place(x=410,y=480, height=30, width=155)

# Title the titles for each listbox 4
label4=Label(window, text=classMapKeys[idx+3], background="#282929", fg="#e6e6e6")
label4.place(x=585,y=160, height=30, width=155)
label4.config(font=("Arial Bold", 16))

# Optional text to be implemented for listbox 1
label4a=Label(window, text="", background="#282929", fg="#e6e6e6")
label4a.config(font=("Helvetica", 16))
label4a.place(x=585,y=480, height=30, width=155)

# Classes "Button"
backToClassesButton=Label(window, text="CLASSES", background="#ffcc00", fg="#282929")
backToClassesButton.config(font=("Arial", 22))
backToClassesButton.place(x=330,y=510, height=40, width=140)
backToClassesButton.bind("<Button-1>", backToClassMenu)

# Keep window open
window.mainloop()
