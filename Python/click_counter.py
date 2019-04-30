#click Counter

from tkinter import*

class Application(Frame):
	"""GUI Application that counts button clicks"""
	def __init__(self, master):
		"""Initialize the frame"""
		super(Application, self).__init__(master)
		self.grid()
		self.bttn_clicks = 0
		self.create_widgets()
		
	def create_widgets(self):
		"""Create button which displays numbers of clicks"""
		self.bttn = Button(self)
		self.bttn["text"] = "Total clicks: 0"
		self.bttn["command"] = self.update_count
		self.bttn.grid()
	
	def update_count(self):
		"""Increase click count"""
		self.bttn_clicks += 1
		self.bttn["text"] = "Total Clicks: " + str(self.bttn_clicks)
		
root = Tk()
root.title("Click Counter")
root.geometry("200x50")

app = Application(root)

root.mainloop()