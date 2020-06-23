import tkinter as tki
import tkinter.messagebox

gui = tki.Tk()

gui.geometry("400x400")

gui.title("button")

label = tki.Label(gui, text = "button")
label.pack()

def clicked():

    tki.messagebox.showinfo("Message", "this is coded in python") 
    

button = tki.Button(gui, text = "click me", command = clicked)
button.pack()

gui.mainloop()