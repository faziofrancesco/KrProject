from tkinter import *
import mznSolver

root = Tk()

#, Label(root, text="Value2:"), Label(root, text="Value3:"), Label(root, text="Value4:"), Label(root, text="Value5:")
labels = []
nJobsLabel = Label(root, text="Type the number of jobs:")

nJobsEntry = Entry(root)
# , Entry(root), Entry(root), Entry(root), Entry(root)
entries = []

print("ENTRY = ", nJobsEntry.get())
nJobsLabel.pack()
nJobsEntry.pack()

for label, entry in zip(labels, entries):
    label.pack()
    entry.pack()

def calculate():
    p = []
    for e in entries:
        p.append(int(e.get()))
    mznSolver.singleMachine(int(nJobsEntry.get()),p)
    print([entry.get() for entry in entries])

def command():
    #print([entry.get() for entry in entries])
    print("ENTRY = ", nJobsEntry.get())
    for i in range(int(nJobsEntry.get())):
        labels.append(Label(root, text="Process time job "+str(i)))
        entries.append(Entry(root))
    for label, entry in zip(labels, entries):
        label.pack()
        entry.pack()

    Button(root, text="Print jobs", command=calculate).pack()

Button(root, text="Confirm n jobs", command=command).pack()

root.mainloop()