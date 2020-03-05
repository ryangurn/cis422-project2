from tkinter import *
from tkinter.ttk import Notebook,Entry

class ClassRoadmap(tk.Tk):
    def __init__(self, master):

		self.idx = 0

 		self._lightGrey = "#b8b8b8"
        self._grey = "#323232"
        self._darkGrey = "#282929"
        self._yellow = "#ffcc00"
        self._green = "#369148"
        self._button = "<Double-Button-1>"
        self._buttonHeight = 30
        self._buttonWidth = 60
        self._buttonText = ("Arial Bold", 16)

        self.master = master
        self.window = Frame(master, bg = self._darkGrey, height = 600, width = 800)
        self.window.place(x = 0, y = 0)

        # Empty list that will store the class keys in same order as dictionary
		self.classMapKeys = []

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
			self.classMapKeys.append([key for key in classMap.keys()][i])


		# Lower (dark) half of the window
		self.labelNext=Label(self.window, text="", background="#282929", fg="#e6e6e6")
		self.labelNext.place(x=0,y=125, height=475, width=800)

		# Green Stripe
		self.labelNext=Label(self.window, text="", background="#369148", fg="#e6e6e6")
		self.labelNext.place(x=0,y=122, height=8, width=800)

		# RoadMap Text
		self.roadMapLabel = Label(self.window, text="ROADMAP", background="#323232", fg="#ffcc00")
		self.roadMapLabel.place(x=-150,y=5, height=115, width=600)
		self.roadMapLabel.config(font=("Helvetica", 37))

		# UO Logo
		self.image = PhotoImage(file="UOicon.gif")
		self.label = Label(image = image)
		self.label.place(x=670,y=5)


		# Initializes listboxes 1
		self.listBx1 = Listbox(self.window, background="#323232", selectbackground="#369148", fg="#e6e6e6")
		self.listBx1.place(x=60,y=195, height=285, width=155)

		# Initializes listboxes 2
		self.listBx2 = Listbox(self.window, background="#323232", selectbackground="#369148", fg="#e6e6e6")
		self.listBx2.place(x=235,y=195, height=285, width=155)

		# Initializes listboxes 3
		self.listBx3 = Listbox(self.window, background="#323232", selectbackground="#369148", fg="#e6e6e6")
		self.listBx3.place(x=410,y=195, height=285, width=155)

		# Initializes listboxes 4
		self.listBx4 = Listbox(self.window, background="#323232", selectbackground="#369148", fg="#e6e6e6")
		self.listBx4.place(x=585,y=195, height=285, width=155)

		# Populates all the listboxes
		self.box1_update()
		self.box2_update()
		self.box3_update()
		self.box4_update()

		# "Next" Button
		self.labelNext=Label(self.window, text="NEXT", background="#282929", fg="#e6e6e6")
		self.labelNext.config(font=("Arial", 12))
		self.labelNext.place(x=750,y=280, height=20, width=40)

		# "Prev" Button
		self.labelPrev=Label(self.window, text="PREV", background="#282929", fg="#e6e6e6")
		self.labelPrev.config(font=("Arial", 12))
		self.labelPrev.place(x=10,y=280, height=20, width=40)

		# if the data doesn't have at least 4 quarters of data, grey out "Next" button
		if(len(self.classMapKeys) <= 4):
			self.buttonNext=Label(self.window, text=">", background="#808080", fg="#e6e6e6")
			self.buttonNext.config(font=("Arial Bold", 22))
			self.buttonNext.place(x=750,y=300, height=40, width=40)
			self.buttonNext.bind("<Button-1>", self.update_next)
		else:
			# Set to green if it doesn't
			self.buttonNext=Label(self.window, text=">", background="#369148", fg="#e6e6e6")
			self.buttonNext.config(font=("Arial Bold", 22))
			self.buttonNext.place(x=750,y=300, height=40, width=40)
			self.buttonNext.bind("<Button-1>", self.update_next)

		# If the index is 0, grey out the "Prev" button
		if(self.idx == 0):
			self.buttonPrev=Label(self.window, text="<", background="#808080", fg="#e6e6e6")
			self.buttonPrev.config(font=("Arial Bold", 22))
			self.buttonPrev.place(x=10,y=300, height=40, width=40)
			self.buttonPrev.bind("<Button-1>", self.update_prev)
		else:
			# Set to green if it doesn't
			self.buttonPrev=Label(self.window, text="<", background="#369148", fg="#e6e6e6")
			self.buttonPrev.config(font=("Arial Bold", 22))
			self.buttonPrev.place(x=10,y=300, height=40, width=40)
			self.buttonPrev.bind("<Button-1>", self.update_prev)


		# Title the titles for each listbox 1
		self.label1=Label(self.window, text=self.classMapKeys[self.idx], background="#282929", fg="#e6e6e6")
		self.label1.config(font=("Arial Bold", 16))
		self.label1.place(x=60,y=160, height=30, width=155)

		# Optional text to be implemented for listbox 1
		self.label1a=Label(self.window, text="", background="#282929", fg="Green")
		self.label1a.config(font=("Helvetica", 16))
		self.label1a.place(x=60,y=480, height=30, width=155)

		# Title the titles for each listbox 2
		self.label2=Label(self.window, text=self.classMapKeys[self.idx+1], background="#282929", fg="#e6e6e6")
		self.label2.config(font=("Arial Bold", 16))
		self.label2.place(x=235,y=160, height=30, width=155)

		# Optional text to be implemented for listbox 1
		self.label2a=Label(self.window, text="", background="#282929", fg="#e6e6e6")
		self.label2a.config(font=("Helvetica", 16))
		self.label2a.place(x=235,y=480, height=30, width=155)

		# Title for each listbox 3
		self.label3=Label(self.window, text=self.classMapKeys[self.idx+2], background="#282929", fg="#e6e6e6")
		self.label3.config(font=("Arial Bold", 16))
		self.label3.place(x=410,y=160, height=30, width=155)

		# Optional text to be implemented for listbox 1
		self.label3a=Label(self.window, text="", background="#282929", fg="white")
		self.label3a.config(font=("Helvetica", 16))
		self.label3a.place(x=410,y=480, height=30, width=155)

		# Title the titles for each listbox 4
		self.label4=Label(self.window, text=self.classMapKeys[self.idx+3], background="#282929", fg="#e6e6e6")
		self.label4.place(x=585,y=160, height=30, width=155)
		self.label4.config(font=("Arial Bold", 16))

		# Optional text to be implemented for listbox 1
		self.label4a=Label(self.window, text="", background="#282929", fg="#e6e6e6")
		self.label4a.config(font=("Helvetica", 16))
		self.label4a.place(x=585,y=480, height=30, width=155)

		# Classes "Button"
		self.backToClassesButton=Label(self.window, text="CLASSES", background="#ffcc00", fg="#282929")
		self.backToClassesButton.config(font=("Arial", 22))
		self.backToClassesButton.place(x=330,y=510, height=40, width=140)
		self.backToClassesButton.bind("<Button-1>", self.backToClassMenu)


		def box1_update():
		# Updates listbox 1 with class data given the key
			for i in range(len(self.classMap[self.classMapKeys[self.idx]])):
				self.listBx1.insert(0, classMap[self.classMapKeys[self.idx]][i])


		def box2_update():
		# Updates listbox 2 with class data given the key
			for i in range(len(self.classMap[self.classMapKeys[self.idx+1]])):
				self.listBx2.insert(0, self.classMap[self.classMapKeys[self.idx+1]][i])


		def box3_update():
		# Updates listbox 3 with class data given the key
			for i in range(len(self.classMap[classMapKeys[self.idx+2]])):
				self.listBx3.insert(0, classMap[self.classMapKeys[self.idx+2]][i])

		def box4_update():
		# Updates listbox 4 with class data given the key
			for i in range(len(self.classMap[classMapKeys[self.idx+3]])):
				self.listBx4.insert(0, classMap[self.classMapKeys[self.idx+3]][i])


		def update_next(event):
		# Function for the "Next" button
			self.idx
			# Checks to see if end has been reached
			if(self.idx >= (len(self.classMap)-4)):
				return
			else:
				# Sets button to green
				self.buttonPrev.config(background="#369148", fg="#e6e6e6")
				
				if((self.idx >= len(self.classMap)-5)):
					# Sets button to grey
					self.buttonNext.config(background="#808080", fg="#e6e6e6")

				self.idx += 1
				# Erases listboxes
				self.listBx1.delete(0, END)
				self.listBx2.delete(0, END)
				self.listBx3.delete(0, END)
				self.listBx4.delete(0, END)

				# Updates listboxes
				self.box1_update()
				self.box2_update()
				self.box3_update()
				self.box4_update()

				# Modifies the listbox text titles with quarter info
				self.classMapKeys
				self.label1['text'] = self.classMapKeys[self.idx]
				self.label2['text'] = self.classMapKeys[self.idx+1]
				self.label3['text'] = self.classMapKeys[self.idx+2]
				self.label4['text'] = self.classMapKeys[self.idx+3]


		def update_prev(event):
		# Function for the "Prev" button
			self.idx
			# Checks to see if beginning has been reached
			if(self.idx == 0):
				return
			else:
				# Sets button to green
				self.buttonNext.config(background="#369148", fg="#e6e6e6")

				if(self.idx-1 == 0):
					# Sets button to grey
					self.buttonPrev.config(background="#808080", fg="#e6e6e6")

				self.idx -= 1
				# Erases listboxes
				self.listBx1.delete(0, END)
				self.listBx2.delete(0, END)
				self.listBx3.delete(0, END)
				self.listBx4.delete(0, END)

				# Updates listboxes
				box1_update()
				box2_update()
				box3_update()
				box4_update()

				# Modifies the listbox text titles with quarter info
				self.classMapKeys
				self.label1['text'] = self.classMapKeys[self.idx]
				self.label2['text'] = self.classMapKeys[self.idx+1]
				self.label3['text'] = self.classMapKeys[self.idx+2]
				self.label4['text'] = self.classMapKeys[self.idx+3]

		def backToClassMenu(event):
			# Function to go back to the classes menu
			print("Goes back to class menu")
