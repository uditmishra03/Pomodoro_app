from tkinter import *
import math, time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
CSK_YELLOW= "#F1D00A"
TEAL = "#00A19D"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    timer_label.config(text="Timer", fg=TEAL)
    checkmark_label.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # print(reps)
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)

def pause_timer():
    sleep_duration = float(pause_entry.get())*60
    time.sleep(sleep_duration)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "✔"
        checkmark_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


timer_label = Label(text="Timer", fg=TEAL, bg=YELLOW, font=(FONT_NAME, 48, "bold"))
timer_label.grid(column=1, row=0)


# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

checkmark_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME))
checkmark_label.grid(column=1, row=3)
# Buttons

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

pause_label = Label(text="Pause for:", fg=RED, bg=YELLOW, font=(FONT_NAME, 12,))
pause_label.grid(column=0, row=4)
pause_entry = Entry(width=20)
# pause_entry.insert(0, "in minutes")
pause_entry.grid(column=1, row=4, sticky="nw")
pause_minutes_label = Label(text="minutes", fg=RED, bg=YELLOW, font=(FONT_NAME, 10,))
pause_minutes_label.grid(column=1, row=4, sticky="se")
pause_button = Button(text="Pause", highlightthickness=0, command=pause_timer)
pause_button.grid(column=2, row=4)

window.mainloop()
