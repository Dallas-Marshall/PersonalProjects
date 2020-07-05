"""Simple calculator to practice using tkinter by Dallas Marshall."""

from tkinter import *

root = Tk()
root.title("Simple Calculator")

display_bar = Entry(root, width=35, borderwidth=5)
display_bar.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(number, display_bar_current):
    """Add number of button pressed to display bar."""
    display_bar_current.insert(len(display_bar_current.get()), number)


def button_clear():
    """Clear display bar of all inputs."""
    display_bar.delete(0, END)


def plus_button(display_bar_current):
    """Display '+' in the display bar when addition button is pressed."""
    display_bar_current.insert(len(display_bar_current.get()), " + ")


def sum_values(display_bar_current):
    """Sum all values."""
    display_bar_string = display_bar_current.get()
    display_bar_values = display_bar_string.split(" + ")
    sum_value = 0
    for value in display_bar_values:
        sum_value += int(value)
    display_sum_value(sum_value, display_bar_current)


def display_sum_value(sum_value, display_bar_current):
    """Display answer to display bar."""
    display_bar.delete(0, END)
    display_bar_current.insert(0, sum_value)


# Define buttons
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0, display_bar))
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1, display_bar))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2, display_bar))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3, display_bar))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4, display_bar))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5, display_bar))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6, display_bar))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7, display_bar))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8, display_bar))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9, display_bar))

button_add = Button(root, text="+", padx=39, pady=20, command=lambda: plus_button(display_bar))
button_equal = Button(root, text="=", padx=91, pady=20, command=lambda: sum_values(display_bar))
button_clear = Button(root, text="Clear", padx=79, pady=20, command=button_clear)

# Display buttons on screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)

button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

root.mainloop()
