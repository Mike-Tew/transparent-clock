# TODO
# Resize and improve app layout.
# Make images for Play/Pause/Reset buttons.
# Add window title.

from tkinter import Tk, LabelFrame, Label, Button
from datetime import datetime

class Clock(Tk):
    def __init__(self):
        super().__init__()

        self.counter = 28800
        self.running = False
        self.counting_id = None
        self.default_display = "00:00:00"
        self.on_top = False

        self.geometry("300x150+800+300")

        self.timer_frame = LabelFrame(self)
        self.timer_frame.grid(row=0, column=0)

        self.timer_label = Label(
            self.timer_frame, text=self.default_display, font=("Helvetica 20")
        )
        self.timer_label.grid(row=0, column=0, columnspan=3)

        self.start_button = Button(
            self.timer_frame,
            text="Start",
            command=self.start_timer,
        )
        self.start_button.grid(row=1, column=0)

        self.pause_button = Button(
            self.timer_frame, text="Pause", command=self.pause_timer
        )
        self.pause_button.grid(row=1, column=1)

        self.reset_button = Button(
            self.timer_frame, text="Reset", command=self.reset_timer
        )
        self.reset_button.grid(row=1, column=2)

        self.opacity_frame = LabelFrame(self, text="Opacity")
        self.opacity_frame.grid(row=0, column=1, padx=[20, 0])

        self.increase_opacity_button = Button(
            self.opacity_frame,
            text="+",
            width=2,
            font=("Helvetica 15"),
            command=self.increase_opacity,
        )
        self.increase_opacity_button.grid(row=0, column=3)

        self.decrease_opacity_button = Button(
            self.opacity_frame,
            text="-",
            width=2,
            font=("Helvetica 15"),
            command=self.decrease_opacity,
        )
        self.decrease_opacity_button.grid(row=1, column=3)

        self.on_top_button = Button(
            self, text="Always On Top", command=self.always_on_top
        )
        self.on_top_button.grid(row=0, column=2)

        self.attributes("-alpha", 0.9)

    def counting(self):
        print("I am running.")

        if self.running:
            timer_timestamp = datetime.fromtimestamp(self.counter)
            label_text = timer_timestamp.strftime("%H:%M:%S")
            self.timer_label.config(text=label_text)
            self.counter += 1

        self.counting_id = self.timer_label.after(1000, self.counting)

    def start_timer(self):
        """Start and display the timer."""

        self.running = True
        self.counting()
        self.start_button["state"] = "disabled"
        self.pause_button["state"] = "normal"
        self.reset_button["state"] = "normal"

    def pause_timer(self):
        """Pause and display the timer."""

        self.running = False
        self.timer_label.after_cancel(self.counting_id)
        self.counter -= 1

        self.start_button["state"] = "normal"
        self.pause_button["state"] = "disabled"
        self.reset_button["state"] = "normal"

    def reset_timer(self):
        """Reset and display the timer."""

        self.running = False
        self.counter = 28800
        self.timer_label.after_cancel(self.counting_id)
        self.timer_label.config(text=self.default_display)

        self.start_button["state"] = "normal"
        self.pause_button["state"] = "disabled"
        self.reset_button["state"] = "disabled"

    def increase_opacity(self):
        """Increase the opacity of the app."""

        self.decrease_opacity_button["state"] = "normal"
        opacity = self.attributes()[1]

        if opacity >= 1:
            self.increase_opacity_button["state"] = "disabled"
        else:
            self.attributes("-alpha", opacity + 0.1)

    def decrease_opacity(self):
        """Decrease the opacity of the app."""

        self.increase_opacity_button["state"] = "normal"
        opacity = self.attributes()[1]

        if opacity <= 0.2:
            self.attributes("-alpha", 0.1)
            self.decrease_opacity_button["state"] = "disabled"
        else:
            self.attributes("-alpha", opacity - 0.1)

    def always_on_top(self):
        if self.on_top == False:
            self.on_top = True
            self.attributes("-topmost", True)
            self.on_top_button.config(fg="red")
        else:
            self.on_top = False
            self.attributes("-topmost", False)
            self.on_top_button.config(fg="black")


if __name__ == "__main__":
    clock = Clock()
    clock.mainloop()
