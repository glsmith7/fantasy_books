# import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


root = ttk.Window(themename="pulse")

b1 = ttk.Checkbutton(bootstyle="toolbutton-danger", text ="Click 3")
b1.grid(row=0, column = 0,padx=5, pady=10)

b2 = ttk.Button(root, text="Submit", bootstyle="info",)
b2.grid(row=0, column = 1, padx=5, pady=10)

b3 = ttk.Checkbutton(text="Submit",state=1)
b3.grid(row=0, column = 2, padx=5, pady=10)

b4 = ttk.Checkbutton(bootstyle="outline-toolbutton-dark", text ="Click 4")
b4.grid(row=0, column = 3, padx=5, pady=10)

b5 = ttk.Checkbutton(bootstyle="success-round-toggle", text ="Click 5")
b5.grid(row=0, column = 4, padx=5, pady=10)

b6 = ttk.Checkbutton(bootstyle="warning-square-toggle", text ="Click 6")
b6.grid(row=1, column=0, padx=5, pady=10)

b7 = ttk.Checkbutton(text ="Click 7", state = "disabled")
b7.grid(row=1, column=1, padx=5, pady=10)

b8 = ttk.Combobox(values=[1,2,3],state="readonly")
b8.grid(row=1, column=2, padx=5, pady=10)

b9 = ttk.DateEntry(bootstyle="dark") # print(cal.entry.get()) is the syntax for reading.
b9.grid(row=1, column=3, padx=5, pady=10)

b10 = ttk.Progressbar(value=50)
b10.grid (row=1, column=4, padx=5, pady=10)

b11 = ttk.Entry()
b11.grid(row=2, column = 0,padx=5, pady=10)

b12 = ttk.Floodgauge(value=30)
b12.grid(row=2, column = 1, padx=5, pady=10)

b13 = ttk.Frame(bootstyle="danger")
b13.grid(row=2, column = 2, padx=5, pady=10)

b14 = ttk.Label(bootstyle="warning", text ="Click 9")
b14.grid(row=2, column = 3, padx=5, pady=10)

b15 = ttk.Label(bootstyle="inverse-success", text ="Click 5")
b15.grid(row=2, column = 4, padx=5, pady=10)

b16 = ttk.Labelframe(bootstyle="danger",text="danger")
b16.grid(row=3, column=0, padx=5, pady=10)

b17 = ttk.Menubutton(text ="Click 7")
b17.grid(row=3, column=1, padx=5, pady=10)

b18 = ttk.Meter(bootstyle="success", subtextstyle="warning",amountused=115,amounttotal=200,textleft="Use", textright="of Total")
b18.grid(row=3, column=2, padx=5, pady=10)

b19 = ttk.Notebook(bootstyle="dark",)
b19.grid(row=3, column=3, padx=5, pady=10)

#b20 not used

b21 = ttk.Panedwindow(bootstyle="info")
b21.grid(row=4, column = 0,padx=5, pady=10)

b22 = ttk.Progressbar(bootstyle="success-striped",value=95)
b22.grid(row=4, column = 1, padx=5, pady=10)

b23 = ttk.Radiobutton(bootstyle="danger", text="Yaas")
b23.grid(row=4, column = 2, padx=5, pady=10)

b24 = ttk.Radiobutton(bootstyle="toolbutton-warning", text ="Click A")
b24.grid(row=4, column = 3, padx=5, pady=10)

b25 = ttk.Scale(bootstyle="success")
b25.grid(row=4, column = 4, padx=5, pady=10)

b26 = ttk.Labelframe(bootstyle="danger",text="danger")
b26.grid(row=5, column=0, padx=5, pady=10)

b27 = ttk.Menubutton(text ="Click 7")
b27.grid(row=5, column=1, padx=5, pady=10)

b28 = ttk.Meter(bootstyle="success", subtextstyle="warning",amountused=115,amounttotal=200,textleft="Use", textright="of Total")
b28.grid(row=5, column=2, padx=5, pady=10)

b29 = ttk.Notebook(bootstyle="dark",)
b29.grid(row=5, column=3, padx=5, pady=10)
root.mainloop()