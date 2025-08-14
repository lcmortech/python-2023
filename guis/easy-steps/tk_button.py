from tkinter import *

#created window, specified a title
window = Tk()
window.title("Button Example (widget)")

#exits the program when clicked
btn_end = Button(window, text = "Close", command = exit)

#toggles window bg color
def tog():
    if window.cget("bg") == "yellow":
        window.configure(bg = "gray")
    else:
        window.configure(bg = "yellow")

#creates a button to call toggle function
btn_tog = Button(window, text = "Switch", command = tog)