import tkinter

window = tkinter.Tk()#create a window
window.title("My first GUI program")# add a title for the window
window.minsize(width=500, height=300)#set the minisize for the window
window.config(padx=20, pady=20) #add paddings to the whole window around those widgets

#label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold")) # create a lable
#tkiner layout manager: pack,place,grid
# my_label.pack() # make the label appear on the window,from top to bottom, one by one
# my_label.place(x=100, y=20)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# my_label.pack()
# my_label["text"] = "New Text"
# my_label.config(text="New Text")

#button
def button_clicked():
    # print("I got clicked")
    new_input = input.get()
    my_label["text"] = new_input

my_button = tkinter.Button(text="click me", command=button_clicked)
my_button.grid(column=1, row=1)
# my_button.pack()

my_button2 = tkinter.Button(text="button2")
my_button2.grid(column=2, row=0)

# entry
input = tkinter.Entry(width=10)
input.grid(column=3, row=2)
# input.pack()




# import turtle
# tim = turtle.Turtle()
# tim.write()

window.mainloop() # listening whether the user wants to do anything