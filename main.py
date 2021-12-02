from tkinter import *
import mznSolver

root = Tk()

OptionList = [
"Single Machine",
"Single Machine with weight",
"Multiple Machine",
"Multiple Machine with tags"
] 

first = StringVar(root)
first.set(OptionList[0])
option = OptionMenu(root, first, *OptionList)
option.pack()

def callback(*args):
    if(first.get() == "Single Machine"):
        Button(root, text="Confirm", command=optionSM).pack()
    elif(first.get() == "Multiple Machine"):
        Button(root, text="Confirm", command=optionMM).pack()

first.trace("w", callback)

def optionSM():

    labels = []
    nJobsLabel = Label(root, text="Type the number of jobs:")
    nJobsEntry = Entry(root)

    entries = []

    nJobsLabel.pack()
    nJobsEntry.pack()
   
    Button(root, text="Confirm n jobs", command=commandSM(labels,entries,nJobsEntry)).pack()

def optionMM():
    
    labels = []
    nJobsLabel = Label(root, text="Type the number of jobs:")
    nJobsEntry = Entry(root)

    nMachinesLabel = Label(root, text="Type the number of machines:")
    nMachinesEntry = Entry(root)

    entries = []

    nJobsLabel.pack()
    nMachinesLabel.pack()
    nJobsEntry.pack()
    nMachinesEntry.pack()

    for label, entry in zip(labels, entries):
        label.pack()
        entry.pack()

    Button(root, text="Confirm n jobs and m machines", command=commandMM(labels,entries,nJobsEntry,nMachinesEntry)).pack()



def calculateMM(entries,nJobsEntry,nMachinesEntry):
    p = []
    for e in entries:
        p.append(int(e.get()))

    mznSolver.multipleMachine(int(nJobsEntry.get()),int(nMachinesEntry.get()),p)
    print([entry.get() for entry in entries])

def calculateSM(entries,nJobsEntry):
    p = []
    for e in entries:
        p.append(int(e.get()))

    mznSolver.singleMachine(int(nJobsEntry.get()),p)

    print([entry.get() for entry in entries])

def commandSM(labels,entries,nJobsEntry):

    print("ENTRY = ", nJobsEntry.get())
    for i in range(int(nJobsEntry.get())):
        labels.append(Label(root, text="Process time job "+str(i)))
        entries.append(Entry(root))
    for label, entry in zip(labels, entries):
        label.pack()
        entry.pack()

    Button(root, text="Print jobs", command=calculateSM(entries,nJobsEntry)).pack()

def commandMM(labels,entries,nJobsEntry,nMachinesEntry):

    print("ENTRY = ", nJobsEntry.get())
    for i in range(int(nJobsEntry.get())):
        labels.append(Label(root, text="Process time job "+str(i)))
        entries.append(Entry(root))
    for label, entry in zip(labels, entries):
        label.pack()
        entry.pack()

    Button(root, text="Print jobs", command=calculateMM(entries,nJobsEntry,nMachinesEntry)).pack()

root.mainloop()