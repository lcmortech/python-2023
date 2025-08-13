from tkinter import *

#created window, specified a title
window = Tk()
window.title("Button Example (widget)")

#exits the program when clicked
btn_end = Button(window, text = "Close", command = exit)