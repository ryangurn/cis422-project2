import tkinter as tk
from tkinter import *


def createClassList():
    root = tk.Tk()
    root.grid_rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    frame_main = tk.Frame(root, bg="gray")
    frame_main.grid(sticky='news')

    #REFERENCE: https://stackoverflow.com/questions/43731784/tkinter-canvas-scrollbar-with-grid

    #A side bar displaying all the course subjects
    courseSubjects = tk.Frame(frame_main, width=150, bg="gray30", height=500, relief="sunken", borderwidth=2)
    courseSubjects.grid(row=0, column=0, pady=(5, 0), sticky="nw")
    courseSubjects.grid_rowconfigure(0, weight=1)
    courseSubjects.grid_columnconfigure(0, weight=1)
    #this will allow for button resizing later
    courseSubjects.grid_propagate(FALSE)
    #add canvas to the frame
    subjectsCanvas = Canvas(courseSubjects, bg = "gray30")
    subjectsCanvas.grid(row = 0, column = 0, sticky = "news")
    # Link the scrollbar to the canvas
    subjectScroller = tk.Scrollbar(courseSubjects, orient="vertical", command=subjectsCanvas.yview)
    subjectScroller.grid(row=0, column=1, sticky="ns")
    subjectsCanvas.configure(yscrollcommand=subjectScroller.set)

    subjectButtons = tk.Frame(subjectsCanvas, bg="blue", relief = "sunken")
    subjectsCanvas.create_window((0, 0), window=subjectButtons, anchor="nw")
    rows = 200
    columns = 2
    buttons = [[tk.Button() for j in range(columns)] for i in range(rows)]
    for i in range(0, rows):
        for j in range(0, columns):
            buttons[i][j] = tk.Button(subjectButtons, text=("%d,%d" % (i+1, j+1)))
            buttons[i][j].grid(row=i, column=j, sticky="news")

    subjectButtons.update_idletasks()
    subjectsCanvas.config(scrollregion = subjectsCanvas.bbox("all"))

    #The 'central column' displaying the list of classes for a given course subject
    specificCourses = tk.Frame(frame_main, bg = "gray54", width=150, height=500, relief="sunken", borderwidth=2)
    #specificCourses.pack(expand=True, fill='both', side='left', anchor='center')
    specificCourses.grid(row=0, column=2, pady=(5, 0), sticky="nw")
    specificCourses.grid_rowconfigure(0, weight=1)
    specificCourses.grid_columnconfigure(2, weight=1)
    specificCourses.grid_propagate(FALSE)

    courseCanvas = Canvas(specificCourses, bg = "gray32")
    courseCanvas.grid(row = 0, column = 2, sticky = "news")
    courseScroller = tk.Scrollbar(specificCourses, orient = "vertical", command = courseCanvas.yview)
    courseScroller.grid(row = 0, column = 3, sticky = "ns")
    courseCanvas.configure(yscrollcommand = courseScroller.set)

    courseButtons = tk.Frame(courseCanvas, bg = "red", relief = "sunken")
    courseCanvas.create_window((1,1), window = courseButtons, anchor = "nw")
    cButtons = [[tk.Button() for j in range(columns)] for i in range(rows)]
    for i in range(0, rows):
        for j in range(0, columns):
            cButtons[i][j] = tk.Button(courseButtons, text=("%d,%d" % (i+1, j+1)))
            cButtons[i][j].grid(row=i, column=j, sticky="news")
    courseButtons.update_idletasks()
    courseCanvas.config(scrollregion = courseCanvas.bbox("all"))
    #The section of the window with information regarding the course
    courseBio = tk.Frame(root, bg='gray30', width=500, height=500, relief = "sunken")
    courseBio.pack(expand=True, fill='both', side='right')
    courseBio.grid(row = 0, column = 4)


    root.mainloop()

def main():
    createClassList()

main()
