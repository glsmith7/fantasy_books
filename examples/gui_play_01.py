# for scratch work

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

colors_selection = ['Papaya whip','Alice Blue','Aquamarine']

def click_me():
    the_label.configure (text = "Hello " + the_name.get() + "! You picked " + the_number.get())

def radio_button_do():
    chosen_value = radio_variable.get()
    win.configure(background = colors_selection[chosen_value])

    # if chosen_value == 1: win.configure(background = colors_selection[0])
    # elif chosen_value == 2: win.configure(background = colors_selection[1])
    # elif chosen_value == 3: win.configure(background = colors_selection[2])

# DEFINE THE GUI


## Main window
win = tk.Tk()
win.title("Testing 1")

win.resizable(True,True)

## a label
the_label = ttk.Label(win, text="Hello buddy. This is a huge test.")
the_label.grid(column=0,row=0)

# a click button
the_button = ttk.Button(win,text="Click this", command = click_me)
the_button.grid(column = 1, row=0)
the_button.configure(state='enabled')

# a text field
the_name = tk.StringVar()
name_box = ttk.Entry(win,width=50,textvariable=the_name)
name_box.grid(column=0,row=1)

# a combobox
the_number = tk.StringVar()
number_box = ttk.Combobox(win,width=12,textvariable=the_number, state='readonly')
number_box['values'] = (1,2,4,42,51,10432)
number_box.current(3) # index number of the 'values'
number_box.grid(column=2,row=0)
name_box.focus()

# three click boxes
first_check_var = tk.IntVar()
second_check_var = tk.IntVar()
third_check_var = tk.IntVar()

first_box = tk.Checkbutton(win, text = 'Disabled', variable = first_check_var, state = 'disabled')
first_box.select()

second_box = tk.Checkbutton(win, text = 'Unchecked', variable = second_check_var)
second_box.deselect()

third_box = tk.Checkbutton(win, text = 'Checked', variable = third_check_var)
third_box.select()

first_box.grid(column =1, row = 2)
second_box.grid(column =2, row = 2)
third_box.grid(column =3, row = 2)

# three radiobuttons

radio_variable = tk.IntVar()

for color in range(3):
    radio_but = tk.Radiobutton(win,text=colors_selection[color], variable = radio_variable, value = color, command = radio_button_do)
    radio_but.grid(column=color, row = 5, sticky = tk.E)

# scrolled text

scroll_x = 30
scroll_y = 5

nb = scrolledtext.ScrolledText (win, width = scroll_x, height = scroll_y, wrap = tk.WORD)
nb.grid(row=4,columnspan=2)
# greeting.pack()

# FUNCTIONS




# DISPLAY GUI
win.mainloop()

