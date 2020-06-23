import tkinter as tk

gui = tk.Tk();

gui.geometry("400x400")

gui.configure(bg = 'cyan')

gui.title("label")

label = tk.Label(gui, text = "hello world")

label2 = tk.Label(gui, text = "hello K.A.")

label.pack()
label2.pack()
gui.mainloop()