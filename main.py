import time
import tkinter as tk

work_time = 25
short_break_time = 5
long_break_time = 20
repeats = 0
timer_count = None


# timer reset
def reset_timer():
    global repeats

    root.after_cancel(timer_count)
    status.config(text="  WORK  ", fg="white")
    timer.config(text="  00:00  ")
    check.destroy()
    repeats = 0


# timer mechanism
def start_timer():
    global repeats
    repeats += 1

    if repeats in [1, 3, 5, 7]:
        count_down(work_time)
        status.config(text="  WORK  ", fg="green")

    elif repeats in [2, 4, 6]:
        count_down(short_break_time)
        status.config(text="  BREAK  ", fg="pink")

    elif repeats == 8:
        count_down(long_break_time)
        status.config(text="  BREAK  ", fg="red")


# countdown mechanism
def count_down(count):
    global repeats
    global timer_count

    count_minutes = count // 60

    count_seconds = count % 60

    if len(str(count_seconds)) == 2:
        timer.config(text=f"  {count_minutes}:{count_seconds}  ")
    elif len(str(count_seconds)) == 1:
        timer.config(text=f"  {count_minutes}:0{count_seconds}  ")

    if count > 0:
        timer_count = root.after(100, count_down, count - 1)
    else:
        if repeats % 2 == 0:
            check_mark = "☑️    "
            check.config(text=check_mark*(repeats//2))
            check.place(x=120, y=350)
        start_timer()


# UI setup
root = tk.Tk()
root.minsize(width=400, height=450)
root.configure(bg="white")
root.title("Pomodoro Timer")

canvas = tk.Canvas(width=1000, height=1000, bg="#F6FFA4")
canvas.place(x=0, y=-17)
image = tk.PhotoImage(file="tomato_image.png")
canvas.create_image(200, 200, image=image)

title = tk.Label(text="POMODORO TIMER", font=("Chalkboard", 40, "bold"))
title.place(x=11, y=11)

timer = tk.Label(text="  25:00  ", font=("Chalkboard", 30, "bold"))
timer.place(x=49.5, y=295)

status = tk.Label(text=" BREAK ", font=("Chalkboard", 30, "bold"))
status.place(x=222, y=295)

start_button = tk.Button(text="START", font=("Chalkboard", 20, "bold"), command=start_timer)
start_button.place(x=50, y=400)

stop_button = tk.Button(text="STOP", font=("Chalkboard", 20, "bold"))
stop_button.place(x=155, y=400)

reset_button = tk.Button(text="RESET", font=("Chalkboard", 20, "bold"), command=reset_timer)
reset_button.place(x=250, y=400)

check = tk.Label()


root.mainloop()
