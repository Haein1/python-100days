from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
# 25
SHORT_BREAK_MIN = 5
# 5
LONG_BREAK_MIN = 20
reps = 0
CHECK_MARK = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global CHECK_MARK

    window.after_cancel(timer)  #stop the count down
    # timer_text 00:00
    canvas.itemconfig(timer_text, text="00:00")
    #title_label "Timer"
    label_timer.config(text="Timer", fg=GREEN)
    #reset check_marks
    CHECK_MARK = ""
    label_check_mark.config(text=CHECK_MARK)

    #reset  reps
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    # count_down
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        label_timer.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        label_timer.config(text="Break", fg=PINK)
        count_down(short_break_sec)

    else:
        label_timer.config(text="Work", fg=GREEN)
        count_down(work_sec)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global CHECK_MARK

    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1) # COUNT DOWN
    else:
        start_timer()
        if reps % 2 == 0:
            CHECK_MARK += "✔"
            label_check_mark.config(text=CHECK_MARK, fg=GREEN)
# import time
# #
# # count = 5
# # while True:
# #     time.sleep(1)
# #     count -= 1


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW) # https://colorhunt.co/
#bg change color

# def say_something(a, b, c):
#     print(a)
#     print(b)
#     print(c)
# window.after(1000, say_something, 3, 5, 8)


#disply tomato and  text using canvas
#canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)#bg: backgroung color
#highlightthickness=0 make the border around label and button disappear
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)#x=100,y=112, location
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)



#label
label_timer = Label(text="Timer", fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 40, "bold"))
label_timer.grid(column=1, row=0)

label_check_mark = Label(bg=YELLOW, highlightthickness=0)
# text="✔", fg=GREEN
label_check_mark.grid(column=1, row=3)

#button
button_start = Button(text="Start", command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", command=reset_timer) #command: bind the button with a function
button_reset.grid(column=2, row=2)

window.mainloop()