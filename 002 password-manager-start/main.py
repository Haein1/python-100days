from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ------search -------
def find_password():
    website = entry_website.get()
    # print(website)
    try:
        # with open("data.json", "r") as datafile
        datafile = open("data.json", "r")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        data = json.load(datafile)
        if website in data.keys():
            password = data[website]["password"]
            email = data[website]["email"]
            # print(data[website]["password"])
            messagebox.showinfo(title="Password", message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message="No details for the website exists")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    letter_list = [random.choice(letters) for char in range(nr_letters)]

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    symbol_list = [random.choice(symbols) for char in range(nr_symbols)]

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    number_list = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = letter_list + symbol_list + number_list

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char

    password = "".join(password_list)

    entry_password.delete(0, END)
    entry_password.insert(0, password)
    # entry_password.set(f"{password}")
    # print(f"Your password is: {password}")

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # print(entry_website.get())
    # print(entry_email.get())
    # print(entry_password.get())

    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()

    new_data = {
        website:
            {
                "email": email,
                "password": password
            }
    }

    # messagebox.showinfo(title="Title", message="Message")\
    if len(entry_website.get())==0 or len(entry_password.get())==0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")

    else:
        try:
            data_file = open("data.json", mode="r")
        except FileNotFoundError:
            data_file = open("data.json", mode="w")
            # saving updated date
            json.dump(new_data, data_file, indent=4)

        else:
            # data = entry_website.get() + " | " +  entry_email.get() + " | " + entry_password.get()
            # data_file.write(data + "\n")

            # write data, mode:w
            # json.dump(new_data, data_file, indent=4)

            # read data  mode: r
            # data = json.load(data_file)
            # print(data)
            # print(type(data))

            # update data
            # reading old data
            data = json.load(data_file)
            # updating old data with new data
            data.update(new_data)
            #saving updated date
            data_file = open("data.json", mode="w")
            json.dump(data, data_file, indent=4)
            #
            #
        finally:
            entry_website.delete(0, END)
            entry_password.delete(0, END)







        # with open("data.json", mode="r") as data_file:
        #     # data = entry_website.get() + " | " +  entry_email.get() + " | " + entry_password.get()
        #     # data_file.write(data + "\n")
        #
        #     #write data, mode:w
        #     # json.dump(new_data, data_file, indent=4)
        #
        #     #read data  mode: r
        #     # data = json.load(data_file)
        #     # print(data)
        #     # print(type(data))
        #
        #     #update data
        #     #reading old data
        #     data = json.load(data_file)
        #     #updating old data with new data
        #     data.update(new_data)

        # with open("data.json", mode="w") as data_file:
        #
        #     #saving updated date
        #     json.dump(data, data_file, indent=4)
        #
        #
        #     entry_website.delete(0, END)
        #     entry_password.delete(0, END)
# website
# email
# password

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.minsize(width=400, height=400)
window.config(padx=50, pady=50)

#row 0
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

#row 1
label_website = Label(text="Website: ")
label_website.grid(column=0, row=1)
#Entries
entry_website = Entry(width=50)
#Add some text to begin with
# entry.insert(END, string="Some text to begin with.")
#Gets text in entry
# print(entry.get())

entry_website.focus() #make the cursor appear at the "entry_website" while running the app

entry_website.grid(column=1, row=1, columnspan=2)

button_search = Button(text="Search", width=15, command=find_password)
button_search.grid(column=2, row=1)

#ROW 2
label_email_username = Label(text="Email/Username: ")
label_email_username.grid(column=0, row=2)

entry_email = Entry(width=50) #35
entry_email.insert(0, "1422365825@qq.com")
# insert text "1422365825@qq.com" on entry_email from the first character

# print(entry_email.get())
entry_email.grid(column=1, row=2, columnspan=2)

#row 3
label_password = Label(text="Password:")
label_password.grid(column=0, row=3)

entry_password = Entry(width=50)
entry_password.grid(column=1, row=3, columnspan=2)

button_password = Button(text="Generate Password", command=generate_password)
button_password.grid(column=2, row=3)


#row4
button_add = Button(text="Add", width=44, command=save)
button_add.grid(column=1, row=4,columnspan=2)

window.mainloop()
