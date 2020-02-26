import tkinter as tk
from tkinter import *

root = tk.Tk()
root.grid_rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

frame_main = tk.Frame(root, bg="gray")
frame_main.grid(sticky='news')

#https://stackoverflow.com/questions/43731784/tkinter-canvas-scrollbar-with-grid

#A side bar displaying all the course subjects
courseSubjects = tk.Frame(frame_main, width=150, bg='gray30', height=500, relief='sunken', borderwidth=2)
courseSubjects.grid(row=0, column=0, pady=(5, 0), sticky='nw')
courseSubjects.grid_rowconfigure(0, weight=1)
courseSubjects.grid_columnconfigure(0, weight=1)
#this will allow for button resizing later
courseSubjects.grid_propagate(FALSE)
#add canvas to the frame
csCanvas = Canvas(courseSubjects, bg = "gray30")
csCanvas.grid(row = 0, column = 0, sticky = 'news')
# Link a scrollbar to the canvas
vsb = tk.Scrollbar(courseSubjects, orient="vertical", command=csCanvas.yview)
vsb.grid(row=0, column=1, sticky='ns')
csCanvas.configure(yscrollcommand=vsb.set)

frame_buttons = tk.Frame(csCanvas, bg="blue", relief = 'sunken')
csCanvas.create_window((0, 0), window=frame_buttons, anchor='nw')
rows = 200
columns = 2
buttons = [[tk.Button() for j in range(columns)] for i in range(rows)]
for i in range(0, rows):
    for j in range(0, columns):
        buttons[i][j] = tk.Button(frame_buttons, text=("%d,%d" % (i+1, j+1)))
        buttons[i][j].grid(row=i, column=j, sticky='news')

frame_buttons.update_idletasks()
csCanvas.config(scrollregion=csCanvas.bbox("all"))

#The 'central column' displaying the list of classes for a given course subject
specificCourses = tk.Frame(root, bg = 'gray54', width=175, height=500, relief='sunken', borderwidth=2)
specificCourses.pack(expand=True, fill='both', side='left', anchor='center')
specificCourses.grid(row = 0, column = 1)

#The section of the window with information regarding the course
courseBio = tk.Frame(root, bg='gray30', width=500, height=500)
courseBio.pack(expand=True, fill='both', side='right')
courseBio.grid(row = 0, column = 2)


root.mainloop()
