from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from PIL import ImageTk, Image
#import matplotlib.pyplot as plt
def next_page_func():
    import main
    next_page_func.destroy()
  
    
root = tk.Tk()

root.background_image = ImageTk.PhotoImage(Image.open("/Users/aaryabhutkar/Downloads/mini project/wp8379331-desktop-stocks-wallpapers.png"))
root.background_label = tk.Label(root.master, image=root.background_image)
root.background_label.place(relwidth=1, relheight=1)


title_label = tk.Label(root, text="New Budget", font=("Arial", 24), bg="turquoise", fg="black")

# Use pack() method to place the title label at the top of the window
title_label.pack(side='top', padx=5, pady=5)


# Create a frame for the date widgets
date_frame = tk.Frame(root)

# Create the start date label and date widget
start_date_label = tk.Label(date_frame, text="Start Date:", font="Helvetica 12", bg="aquamarine", fg="black")
start_date_widget = DateEntry(date_frame, width=18, background='aquamarine',
                              foreground='black', borderwidth=8)

# Create the end date label and date widget
end_date_label = tk.Label(date_frame, text="End Date:", font="Helvetica 12", bg="aquamarine", fg="black")
end_date_widget = DateEntry(date_frame, width=18, background='aquamarine',
                            foreground='black', borderwidth=8)

# Use pack() method to place the date widgets one below the other
start_date_label.pack(side='top', padx=5, pady=5)
start_date_widget.pack(side='top', padx=5, pady=5)
end_date_label.pack(side='top', padx=5, pady=5)
end_date_widget.pack(side='top', padx=5, pady=5)

# Pack the date frame
date_frame.pack(side='top', padx=10, pady=10)

# Create the label for income
income_label = tk.Label(root, text="Your Budget (In Rupees):", font="Helvetica 12", bg="aquamarine", fg="black")

# Create the entry box for income
income_entry = tk.Entry(root, width=20)

# Use pack() method to place the label and entry box one below the other
income_label.pack(side='top', padx=5, pady=5)
income_entry.pack(side='top', padx=5, pady=5)

#Create a next button

# button = tk.Button(padx=15, pady=5, text='Back', font=('Bold', 12), bg="aqua", fg="black")
# button.pack(side=tk.LEFT, padx=10)
# button.place(relx=0.426, rely=0.55)

button1 = tk.Button(padx=15, pady=5, text='Next', font=('Bold', 12), bg="aqua", fg="black",command=next_page_func)
button1.pack(side=tk.LEFT, padx=10)
button1.place(relx=0.472, rely=0.55)

#Income tax slab
root.geometry("1200x550")



root.mainloop()
