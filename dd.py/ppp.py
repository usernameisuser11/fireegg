from tkinter import *

window = Tk()

photo1 = PhotoImage(file="gif/dog.gif")
label1 = Label(window, image=photo1)
label1.pack()

photo2 = PhotoImage(file="gif/cat.gif")  
label2 = Label(window, image=photo2)
label2.pack()

window.mainloop()