import tkinter as tk

window = tk.Tk()
window.title("Text-to-Speech Converter")
window.geometry('600x400')

# creating widget
label=tk.Label(window,text="Text", bg="blue", height=2,width=40)
label.pack()
# creating text widget
T = tk.Text(window, height=20, width=40, bg = "white")
T.pack(side=tk.LEFT)

tk.mainloop()


