from tkinter import *
from tkinter import messagebox
import csv
import os
import sys

# Initialize name list
nameList = []
numberOfNames = 0

# Opens a .csv file and reads the names from it
# These names are added to nameList
with open('names.csv', 'r') as csv_file:
	csv_reader = csv.reader(csv_file)
	for line in csv_reader:
		# Adds each name to list
		nameList.append(line[0])
		# Updates the number of students in list
		numberOfNames = numberOfNames + 1 
 
def lbPopulate():
# Populates the listbox
	for i in range(0, numberOfNames):
		# Inserts name data into listbox
		lb.insert(i, nameList[i])


def openAddStudentWindow(Event):
# Opens a new window for adding the student
	# Creates a new window over the root window
	print("Work")
	addStudentWindow = Toplevel()
	addStudentWindow.title("Add Student")
	addStudentWindow.geometry("800x600+120+120")
	addStudentWindow.configure(background="#323232")

	siLabel = Label(addStudentWindow, text='')
	siLabel.place(x=0,y=100, height=340, width=800)
	siLabel.config(font=("Mincho Bold", 60))
	siLabel.config(bg="#282929", fg="#262929")


	def onAddStudentClick():
	# Adds student to the .csv file	
		# Gets the name
		name = nameVar.get()

		# If no name has been entered, throw a warning
		if(name == ''):
			messagebox.showwarning("Invalid Name",'Please enter a valid name.')
			return

		# Declare the global variables for modification
		global nameList
		global numberOfNames

		# Update the list of names
		nameList.append(name)

		# Inserts the new name into the listbox
		lb.insert(END, name)

		# Increment the number of names by 1
		numberOfNames = numberOfNames + 1
		labl['text'] = name

		# Writes student name to the csv file and overrides existing one
		with open('names.csv', 'w') as new_file:
			csv_writer = csv.writer(new_file, delimiter=',')
			for i in range(numberOfNames):
				csv_writer.writerow([nameList[i]])

		# Closes the "Add Student" window
		addStudentWindow.destroy()


	newName = Label(addStudentWindow, text='Enter a new name:')
	newName.place(x=170,y=220, height=30, width=220)
	newName.config(bg="#ffcc00", fg="Black")
	newName.config(font=("Arial Bold", 16))

	# Adds text entry box to enter the student's name
	searchbox = Entry(addStudentWindow, textvariable=nameVar)
	searchbox.place(x=350,y=220, height=30, width=200)

	# Button to close the "Add Student" window and go back to main menu
	exitName = Button(addStudentWindow, text='< Back', width=25, command=addStudentWindow.destroy)
	exitName.config(font=("Arial Bold", 20))
	exitName.place(x=0,y=20, height=40, width=140)

	# Button to add the student's name to the csv file
	addName = Button(addStudentWindow, text='Add', width=25, command=onAddStudentClick)
	addName.place(x=560,y=220, height=30, width=70)
	addName.config(font=("Arial Bold", 16))


def onlbclick(event):
# Creates the event when a name is selected in the lisdtbox
    w=event.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    labl['text'] = lb.get(lb.curselection())


def update_listbox(*args):
# Dynamically updates listbox as user types
  search_term = search_var.get()
  lb.delete(0, END)
  for item in all_items:
    if search_term.lower() in item.lower():
      lb.insert(END, item)


# Specifies the window
root = Tk()
root.geometry("800x600+120+120")
root.title("List Box Test")
root.configure(background="#323232")

sLabel = Label(root, text='')
sLabel.place(x=0,y=175, height=340, width=800)
sLabel.config(font=("Mincho Bold", 60))
sLabel.config(bg="#282929", fg="#282929")


# Creates a frame of size 200 by 300 to put the listbox in
fr = Frame(root, width=200, height=200, bg="#369148")

# Place the 200 by 200 listbox here
fr.place(x=300,y=252)

# Creates listbox
lb=Listbox(fr,selectmode="browse",bg="#323232", selectbackground="#05761B")
lb.config(font=("Mincho Bold", 14),fg="#e6e6e6")

# Calls function that populates listbox
lbPopulate()

# Opens name addition menu
'''
button = Button(root, text='Add Student', width=25, command=openAddStudentWindow)
button.place(x=350,y=460, height=20, width=100)
'''

button1 = Label(root, text='')
button1.config(bg="#05781B", fg="#ffcc00")
button1.place(x=348,y=468, height=27, width=106)
button = Label(root, text='Add Student')
button.config(font=("Arial Bold", 13))
button.config(bg="#369148", fg="#ffcc00")
button.place(x=348,y=465, height=27, width=106)
'''

button = Label(root, text='')
button.config(font=("Arial Bold", 16))
button.config(bg="#045E15", fg="#eebb00")
button.place(x=10,y=50, height=5, width=140)
'''

button.bind("<Button-1>", openAddStudentWindow)

# "Search" Label
searchLabel = Label(root, text='Search:')
searchLabel.place(x=290,y=210, height=40, width=80)
searchLabel.config(font=("Arial Bold", 16))
searchLabel.config(bg="#262929", fg="#ffcc00")

'''
# "Student" Label
studentLabel = Label(root, text='Student:')
studentLabel.place(x=260,y=160, height=40, width=80)
studentLabel.config(font=("Arial Bold", 20))
studentLabel.config(bg="#003011", fg="White")

# Student Name Label (Updates)
labl = Label(root, text=' ')
labl.place(x=370,y=160, height=40, width=220)
labl.config(font=("Arial Bold", 20))
labl.config(bg="#003011", fg="White")
'''

# Makes the really cool RegTool title
image = PhotoImage(file="RegToolsLogo.gif")
label = Label(image = image)
label.place(x=100,y=40)

oolsLabel = Label(root, text='')
oolsLabel.place(x=95,y=40, height=5, width=620)
oolsLabel.config(font=("Mincho Bold", 60))
oolsLabel.config(bg="#323232", fg="#323232")

oolsLabel = Label(root, text='')
oolsLabel.place(x=98,y=40, height=90, width=5)
oolsLabel.config(font=("Mincho Bold", 60))
oolsLabel.config(bg="#323232", fg="#323232")

oolsLabel = Label(root, text='')
oolsLabel.place(x=703,y=40, height=90, width=5)
oolsLabel.config(font=("Mincho Bold", 60))
oolsLabel.config(bg="#323232", fg="#323232")

oolsLabel = Label(root, text='')
oolsLabel.place(x=95,y=123, height=5, width=620)
oolsLabel.config(font=("Mincho Bold", 60))
oolsLabel.config(bg="#323232", fg="#323232")


# Creates the search textbox/entrybox
nameVar = StringVar()
search_var = StringVar()
search_var.trace('w', update_listbox)
searchbox = Entry(root, textvariable=search_var, bg="#b8b8b8")
searchbox.place(x=360,y=217, height=26, width=142)
searchbox.config(highlightthickness=0)
# List box geometry
lb.grid(row=1, rowspan=10, column=0,columnspan=5, sticky='W', padx=5, pady=5,ipadx=5, ipady=5)

# Uncomment this line to be able to click  listbox instead of pressing "Return" when the word is highlighted
#lb.bind('<<ListboxSelect>>', onlbclick)

# All items in the listbox get stored in "all_items"
all_items = lb.get(0, END)

# Binds the enter key as selection to the listbox. Calls the onlbclick() function
lb.bind("<Return>", onlbclick)

root.mainloop()

