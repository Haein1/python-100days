import tkinter
from tkinter import *
#TK tutorial
# https://tkdocs.com/tutorial/firstexample.html

#set up the window
#create the window
window = tkinter.Tk()
#give the window a title
window.title("Mike to KM Converter")
#set up the minimum size for the window
window.minsize(width=500, height=300)
#padding set
window.config(padx=20, pady=20)

#create text
#Entries
entry = Entry(width=15)
#Add some text to begin with
entry.insert(END, string="0")
#Gets text in entry
print(entry.get())
# entry.pack()
entry.grid(column=1, row=0)

#Labels
label_miles = Label(text="Miles")
# label_miles.config(text="This is new text")
label_miles.grid(column=2, row=0)

label_2= Label(text="is equal to")
# label_miles.config(text="This is new text")
label_2.grid(column=0, row=1)

label_answer= Label(text="0")
# label_miles.config(text="This is new text")
label_answer.grid(column=1, row=1)

label_3= Label(text="Km")
# label_miles.config(text="This is new text")
label_3.grid(column=2, row=1)

#Buttons
def calculate():
    miles = int(entry.get())
    result = miles/1000
    label_answer.config(text=f"{result}")

#calls action() when pressed
button = Button(text="Calculate", command=calculate)
# button.pack()
button.grid(column=1, row=2)

window.mainloop()