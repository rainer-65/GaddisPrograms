# Source: https://www.geeksforgeeks.org/how-to-use-thread-in-tkinter-python/

# Import Module
from tkinter import *
import time

# Create Object
root = Tk()

# Set geometry
root.geometry("400x400")


def work():

	print("sleep time start")

	for i in range(10):
		print(i)
		time.sleep(1)

	print("sleep time stop")


# Create Button
Button(root, text="Click Me", command=work).pack()

# Execute Tkinter
root.mainloop()
