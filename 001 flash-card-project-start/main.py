from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
current_card = {}
to_learn = {}


#--------------Create new flashcards ------
try:
    words = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = words.to_dict(orient="records")
# print(words)
# print(type(words)) #DataFrane


# print(type(to_learn))
# print(words_dict)
# current_card = {}0
#
# new_words_list = []
# for _ in words_dict:
#     # print(_)
#     dict = {}
#     # print(_["French"])
#     # print(_["English"])
#     dict[_["French"]] = _["English"]
#     new_words_list.append(dict)

# print(new_words_list)


def change_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    # print(current_card)
    # print(current_card["French"])
    # print(current_card["English"])
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(french_text, text=current_card["French"], fill="black")
    canvas.itemconfig(main_image, image=my_image)
    flip_timer = window.after(3000, func=flip_card)
    # global current_card
    # global flip_timer
    # window.after_cancel(flip_timer)
    # rand_int = random.randint(0, len(new_words_list)-1)
    # # print(list(new_words_list[rand_int].keys())[0])
    # # print(type(list(new_words_list[rand_int].keys())[0]))
    # # print(new_words_list[rand_int].items()[0])
    # current_card = new_words_list[rand_int]
    # # current_card = key
    # # print(key)
    # # print(current_card)
    # # print(type(current_card))
    # # print(current_card.keys())
    # # print(type(current_card.keys()))
    # key = list(current_card.keys())[0]
    # canvas.itemconfig(french_text, text=key,fill="black")
    # # canvas.create_text(400, 263, text=french_text, font=WORD_FONT)
    # canvas.itemconfig(card_title, text="French", fill="black")
    # canvas.itemconfig(main_image, image=my_image)
    # flip_timer = window.after(4000, func=flip_card)

# -----flip card --
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="red")
    print(current_card)
    canvas.itemconfig(french_text, text=current_card["English"], fill="red")
    canvas.itemconfig(main_image, image=back_end_image)
    # canvas.itemconfig(card_title, text="English", fill="red")
    # #fill： change the color of the text
    # # print(current_card)
    # value = list(current_card.values())[0]
    # canvas.itemconfig(french_text, text=value, fill="red")
    # canvas.itemconfig(main_image, image=back_end_image)

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    flip_card()
    # print(current_card)
    # # print(new_words_list)
    # # print(words_dict)
    # # print(type(words_dict))
    # new_words_list.remove(current_card)
    # # print(len(new_words_list))
    # data = pandas.DataFrame(new_words_list)
    # data.to_csv("./data/words_to_learn.csv")
    # flip_card()
# --------------UI SET UP ----
window = Tk()
window.title("Flashy")
# window.minsize(width=800, height=700)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR) #BACKGROUND_COLOR

flip_timer = window.after(4000, func=flip_card)

canvas = Canvas(width=800, height=526)
my_image = PhotoImage("./images/card_front.png")
back_end_image = PhotoImage("./images/card_back.png")
main_image = canvas.create_image(400, 263, image=my_image)
# canvas.config(bg=BACKGROUND_COLOR)
card_title = canvas.create_text(400,150, text="French", font=LANGUAGE_FONT)
french_text = canvas.create_text(400, 263, text="", font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)



image_red_x = PhotoImage(file="./images/wrong.png")
button_red_x = Button(image=image_red_x, highlightthickness=0, command=change_word)
button_red_x.grid(row=1, column=0, pady=50)


image_check_mark = PhotoImage(file="./images/right.png")
button_check_mark = Button(image=image_check_mark, highlightthickness=0, command=is_known)
button_check_mark.grid(row=1, column=1, pady=50)


window.mainloop()