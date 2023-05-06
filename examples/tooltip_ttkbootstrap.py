import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.tooltip import ToolTip

app = ttk.Window()
b1 = ttk.Button(app, text="default tooltip")
b1.pack()
b2 = ttk.Button(app, text="styled tooltip")
b2.pack()

# default tooltip
ToolTip(b1, text="This is the default style")

# styled tooltip
ToolTip(b2, text="This is dangerous", bootstyle=(INVERSE, DANGER))

app.mainloop()