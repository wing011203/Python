import sys
from tkinter import *
widget = Button(None, text = 'Hello Widget World', command = sys.exit)
widget.pack()
widget.mainloop()