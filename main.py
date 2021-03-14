from tkinter import Tk, LabelFrame, Label, Button
from datetime import datetime
import time



counter = 28800
running = False
testing = None

def counting():
    global counter
    global running
    print("I am running")
    print(timer_label.after)

    if running == True:
        timer_timestamp = datetime.fromtimestamp(counter)
        label_text = timer_timestamp.strftime("%H:%M:%S")
        timer_label["text"] = label_text
        counter += 1

    global testing
    testing = timer_label.after(1000, counting)



def start_timer(timer_label):
    """Start and display the timer."""

    global running
    running = True
    counting()
    start_button["state"] = "disabled"
    pause_button["state"] = "normal"
    reset_button["state"] = "normal"


def pause_timer():
    """Pause and display the timer."""

    global running
    running = False

    start_button["state"] = "normal"
    pause_button["state"] = "disabled"
    reset_button["state"] = "normal"


def reset_timer():
    """Reset and display the timer."""

    global counter
    global running
    running = False
    counter = 28800

    global testing
    timer_label.after_cancel(testing)

    start_button["state"] = "normal"
    pause_button["state"] = "disabled"
    reset_button["state"] = "disabled"


def increase_opacity(increase_opacity_button):
    """Increase the opacity of the app."""

    decrease_opacity_button["state"] = "normal"
    opacity = root.attributes()[1]

    if opacity >= 1:
        increase_opacity_button["state"] = "disabled"
    else:
        root.attributes("-alpha", opacity + 0.1)


def decrease_opacity(decrease_opacity_button):
    """Decrease the opacity of the app."""

    increase_opacity_button["state"] = "normal"
    opacity = root.attributes()[1]

    if opacity <= 0.2:
        root.attributes("-alpha", 0.1)
        decrease_opacity_button["state"] = "disabled"
    else:
        root.attributes("-alpha", opacity - 0.1)


root = Tk()
root.geometry("300x150+800+300")

timer_frame = LabelFrame(root)
timer_frame.grid(row=0, column=0)

timer_label = Label(timer_frame, text="temp", font=("Helvetica 20"))
timer_label.grid(row=0, column=0, columnspan=3)

start_button = Button(timer_frame, text="Start", command=lambda: start_timer(timer_label))
start_button.grid(row=1, column=0)

pause_button = Button(timer_frame, text="Pause", command=pause_timer)
pause_button.grid(row=1, column=1)

reset_button = Button(timer_frame, text="Reset", command=reset_timer)
reset_button.grid(row=1, column=2)


opacity_frame = LabelFrame(root, text="Opacity")
opacity_frame.grid(row=0, column=1, padx=[20, 0])

increase_opacity_button = Button(
    opacity_frame,
    text="+",
    width=2,
    font=("Helvetica 15"),
    command=lambda: increase_opacity(increase_opacity_button),
)
increase_opacity_button.grid(row=0, column=3)

decrease_opacity_button = Button(
    opacity_frame,
    text="-",
    width=2,
    font=("Helvetica 15"),
    command=lambda: decrease_opacity(decrease_opacity_button),
)
decrease_opacity_button.grid(row=1, column=3)

root.attributes("-alpha", 0.9)
# root.attributes('-topmost', True)
# root.update()

root.mainloop()