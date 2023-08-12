# Source: https://www.geeksforgeeks.org/how-to-use-thread-in-tkinter-python/ (modified)
# Import Module
import time
from _thread import start_new_thread
from tkinter import *

# Create Object
root = Tk()

# Set geometry
root.geometry("400x400")


# work function
def work():
    print("sleep time start")

    for i in range(10):
        print(i)
        time.sleep(1)

    print("sleep time stop")


# use threading
def count():
    # Call work function
    start_new_thread(work, ())


# Create Button
Button(root, text="Click Me", command=count).pack()

# Execute Tkinter
root.mainloop()
