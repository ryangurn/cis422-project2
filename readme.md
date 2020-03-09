# README

## Authors
Authors:

(RegTools)

Joseph Goh

Mason Sayyadi

Owen McEvoy

Ryan Gurnick

Samuel Lundquist

## Creation
Feb 26, 2020

## Project Description
This project is designed to be a class registration and planning assistant primarily for use by University of Oregon advisers. It provides useful information to the adviser and students being advised about which classes are available and which classes the student should take in order to make progress towards graduation. Advisers will also be able to easily structure potential course roadmaps for students' college careers based on major degree requirements and the student's course history. Advisers will also be able to save and manage such information for multiple students for future use. The system will provide course information by web scraping data from classes.uoregon.edu and manage all its data in a local database.

## Compilation & Running
1. Running the main advisor interface
```
> cd <project directory>
> python3 Main.py
```
2. Creating a new database seed (optional)
```
> cd <project directiory>
> python3 DataSeed.py
```

## Dependencies
1. Python 3.7.0 or newer (when using cs computer in DES 100 the command is `python3`)
2. macOS 10.14.6 or newer (same as computers in DES 100)

## Directory Structure
1. `img` - the images directory stores the minor images that allow the GUI to display properly. These images will be displayed at runtime via the GUI.
2. `GUI` - this is the code that defines the user interface and hooks up to the logic and models.
3. `/` - this is the directory where the main logical code goes to setup/seed the database, to connect and interact with the datbase, to parse data from classes.uoregon.edu.
