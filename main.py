from tkinter import *


def increase_opacity():
    """Increase the opacity of the app."""

    opacity = root.attributes()[1]
    root.attributes('-alpha', opacity + 0.1)


def decrease_opacity():
    """Decrease the opacity of the app."""

    opacity = root.attributes()[1]
    if opacity <= 0.2:
        root.attributes('-alpha', 0.1)
    else:
        root.attributes('-alpha', opacity - 0.1)


root = Tk()
root.geometry("200x150+800+300")

timer_frame = LabelFrame(root)
timer_frame.grid(row=0, column=0)

timer_label = Label(timer_frame, text="Timer", font=("Helvetica 20"))
timer_label.grid(row=0, column=0)

start_button = Button(timer_frame, text="")

opacity_frame = LabelFrame(root)
opacity_frame.grid(row=0, column=1)

opacity_up_button = Button(opacity_frame, text="+", width=2, font=("Helvetica 15"), command=increase_opacity)
opacity_up_button.grid(row=0, column=3)

opacity_down_button = Button(opacity_frame, text="-", width=2, font=("Helvetica 15"), command=decrease_opacity)
opacity_down_button.grid(row=1, column=3)

root.attributes('-alpha', 0.9)
# root.attributes('-topmost', True)
# root.update()

root.mainloop()