from tkinter import *

def printkey(event):
	#print(dir(event))
	print("You pressed", '[' + str(event.keycode) + ']' + event.char)

if __name__ == '__main__':
	root = Tk()
	entry = Entry(root)
	entry.bind('<Key>', printkey)
	entry.pack()
	root.mainloop()