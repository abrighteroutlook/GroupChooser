#!/usr/bin/python
#python groupchooser.py
from tkinter import *
import random
import os

root = Tk() #create a GUI window.

version = "0.9"
namesORI = []
group_size_str = StringVar()
group_size_int = ""
usedOnce = False


#----grabs all names from file---------------------------
file = open('students.txt','r') #opens file
namesORI = file.read().splitlines() #adds each line to the list names
file.close() #closes file
#--------------------------------------------------------
size = len(namesORI) #gets amount in file

root.title("Group Chooser " + version) #set the title of window

root.geometry("500x400") #sets size of window
root.resizable(0,0) #makes window un-resizeable

#Functions=========================================

def errormsg():
	def closewin():
		dialog.destroy()
	dialog = Toplevel()
	dialog.title("!")
	dialog.geometry("300x150")
	dialog.resizable(0,0)
	dialog.transient(root)
	dialog.grab_set()
	msg = Label(dialog, text="You have incorrectly/not filled out all the fields")
	msg.pack(padx=20, pady=20)
	exit_b = Button(dialog, text="Okay", command=closewin).pack()
	root.wait_window(dialog)

def showResults(wantedGr,groups,remainders):
	#print("# of wanted sized groups:", wantedGr)
	#print(groups) console testing
	#print("Remainder group: ", remainders)
	solution = LabelFrame(root, text="Groups")
	solution.pack(fill=BOTH, padx=10, pady=10)

	wantedGroups = Label(solution, text="# of wanted sized groups: "+str(wantedGr))
	wantedGroups.pack(side=TOP)
	sortedGroups = Entry(solution)
	sortedGroups.insert(END, groups)
	sortedGroups.pack(fill=X, padx=5)
	remaining = Label(solution, text="Left overs: " + str(remainders))
	remaining.pack(side=BOTTOM)

	usedOnce = True
	

def makeGroups():
	names = list(namesORI)
	groups = []
	remainder = 0

	group_size_int = int(group_size_str.get())
	#print(group_size_int) #test for console

	group_size = group_size_int

	if size % group_size != 0:
		remainder = size % group_size

	wantedGr = size//group_size

	for i in range(wantedGr):
		groups.append([])
		for j in range(group_size):
			groups[i].append("")

	#print(groups) #will print empty name list

	for i in range(len(groups)):
		for j in range(group_size):
			rand_name = random.choice(names)
			groups[i][j] = rand_name
			if rand_name in names: names.remove(rand_name)

	showResults(wantedGr,groups,names)

def checkStatus(): #want to add check to see if int
	if int(group_size_str.get()) > 0:
		if size > 0:
			makeGroups()
	else:
		errormsg()
#=================================================================

mainFrame = LabelFrame(root, text="Group Chooser")
mainFrame.pack(fill=BOTH, padx=10, pady=10)


numOfStudents = Label(mainFrame, text=str(size)+" students in list")
numOfStudents.pack(anchor=NW, pady=10)

entry_label = Label(mainFrame, text="Group Size").pack(anchor=W, side=LEFT)

numOfpplInGroup = Entry(mainFrame, text="Group Size", width=3, textvariable=group_size_str)
numOfpplInGroup.pack(anchor=W, pady=10)
 
create_button = Button(root, text="Create", command=checkStatus).pack(anchor=W, padx=10)

root.mainloop()




