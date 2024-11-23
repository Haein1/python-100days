from tkinter import *
import math
# ---------------------------Constants -----------------------------#
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
CHECK_MARK = ""
timer = None

#------------------------- TIMER RESET ----------------------#
def reset_timer():
    global CHECK_MARK

    #stop the cound down
    window.after_cancel(timer)
    # timer_text 00:00
    canvas.itemconfig(timer_text, text="00:00")
    #title_label " Timer"
    title_label.config(text="Timer", fg=GREEN)
    #reset check marks
    CHECK_MARK = ""
    label_check_mark.config(text=CHECK_MARK)

    #reset reps
    global reps
    reps = 0
#--------------------------- TIMER MECHNISM -----------------------#
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec)


#---------------------------- COUNTDOWN MECHANISM ----------------------#
def count_down(count):
    global CHECK_MARK

    count_min = math.floor(count/60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        if reps%2 == 0:
            CHECK_MARK += "✓"
            label_check_mark.config(text=CHECK_MARK, fg=GREEN )


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("ShaunDoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
shaun_image = PhotoImage(file="tomato.png")
# img = ImageTk.PhotoImage(Image.open(background))
canvas.create_image(100, 112, image=shaun_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME,40,"bold"))
title_label.grid(column=1, row=0)
#image type tkinter can work with

#button
button_start = Button(text="start", command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text="reset", command=reset_timer)
button_reset.grid(column=2, row=2)

#label_check_mark
label_check_mark = Label(bg=YELLOW, highlightthickness=0)
label_check_mark.grid(column=1, row=3)

window.mainloop()