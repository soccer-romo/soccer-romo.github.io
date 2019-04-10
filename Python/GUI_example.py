#GUI Example

import tkinter as tk

root = tk.Tk()

root.title("My Awesom Python GUI")

root.geometry("500x500")
root.resizable(0,0)

welcomeLabel = tk.Label(root,text="Hello World")
welcomeLabel.pack()

countLabel = tk.Label(root,fg="green",text="I'm Here")
countLabel.pack()

counter = 0

def counter_label(label):
	def count():
		global counter
		counter +=1
		label.config(text=str(counter))
		label.after(1000,count)
	count()

counter_label(countLabel)

def exitProgram():
	root.destroy()

exitButton = tk.Button(root, text="Exit", width=25, command=exitProgram)

exitButton.pack()

root.mainloop()