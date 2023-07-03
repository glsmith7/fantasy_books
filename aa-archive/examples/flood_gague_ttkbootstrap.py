import ttkbootstrap as ttk
from ttkbootstrap.constants import *

app = ttk.Window(size=(500, 500))

gauge = ttk.Floodgauge(
    bootstyle=INFO,
    font=(None, 24, 'bold'),
    mask='Memory Used {}%',
)
gauge.pack(fill=BOTH, expand=YES, padx=10, pady=10)

# autoincrement the gauge
gauge.start()

# stop the autoincrement
gauge.stop()

# manually update the gauge value
gauge.configure(value=25)

# increment the value by 10 steps
gauge.step(10)

app.mainloop()