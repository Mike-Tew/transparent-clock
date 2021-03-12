from tkinter import *
import time
x = time.time()
y = time.time()
print(x, y)


running = False


def start_timer():
    """Start and display the timer."""
    print(time.time())


def pause_timer():
    """Pause and display the timer."""
    pass


def reset_timer():
    """Reset and display the timer."""
    pass


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

timer_label = Label(timer_frame, text="00:00:00", font=("Helvetica 20"))
timer_label.grid(row=0, column=0, columnspan=3)

start_button = Button(timer_frame, text="Start", command=start_timer)
start_button.grid(row=1, column=0)

pause_button = Button(timer_frame, text="Pause", command=pause_timer)
pause_button.grid(row=1, column=1)

reset_button = Button(timer_frame, text="Reset", command=reset_timer)
reset_button.grid(row=1, column=2)


opacity_frame = LabelFrame(root, text="Opacity")
opacity_frame.grid(row=0, column=1, padx=[20, 0])

increase_opacity_button = Button(
    opacity_frame, text="+", width=2, font=("Helvetica 15"), command=lambda:increase_opacity(increase_opacity_button)
)
increase_opacity_button.grid(row=0, column=3)

decrease_opacity_button = Button(
    opacity_frame, text="-", width=2, font=("Helvetica 15"), command=lambda:decrease_opacity(decrease_opacity_button)
)
decrease_opacity_button.grid(row=1, column=3)

root.attributes("-alpha", 0.9)
# root.attributes('-topmost', True)
# root.update()

root.mainloop()