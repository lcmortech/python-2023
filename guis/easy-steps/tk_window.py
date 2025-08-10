from tkinter import *

# calls upon contructor to build a new window object:
window = Tk()

# specifies a title for this window
window.title('Label Example')

#calls upon a constructor to create a label object:
label = Label(window, text = "Hello World")

# packer adds the label to the window with both horizontal and vertical padding for positioning:
label.pack(padx = 200, pady = 50)

#mandatory statement to maintain the window by capturing events
window.mainloop() #turns the loop "on"