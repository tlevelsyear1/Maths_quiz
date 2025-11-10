import tkinter as Tk
from tkinter import ttk
import datetime
import random
 
# Window creation.....
window = Tk.Tk()
window.title('Maths Quiz For Kids!')
window.geometry ('700x600')
form_frame = Tk.Frame(window)
form_frame.pack(pady=15)
 
# First Name
ttk.Label(form_frame, text="Enter your Name:", font=("Calibri 24 bold", 11)).grid(row=0, column=0, padx=10, pady=5, sticky="e")
first_name_entry = ttk.Entry(form_frame, width=20)
first_name_entry.grid(row=0, column=1, padx=10, pady=5)
first_name_entry.insert(0, "")
first_name_entry.pack
 
 
#Colours
PASTEL_BLUE = '#AFFAFD'
window.config(bg=PASTEL_BLUE)
 
#function
def subtraction():

    score = 0
    for i in range(4):
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        correct_answer = num1 - num2
        user_answer = int(input(f"{num1} - {num2} = "))
        if user_answer == correct_answer:
            score += 1
    return score
 
 
def addition():

    score = 0

    for i in range(4):
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        correct_answer = num1 + num2
        user_answer = int(input(f"{num1} + {num2} = "))
        if user_answer == correct_answer:
            score += 1
    return score

 
 
#Treeview for scores+
treeview = ttk.Treeview(columns=("Sudent","Score"))
 
treeview.heading("#0", text="Name")
treeview.heading("Score", text="Score(/10)!")
treeview.pack(fill=Tk.BOTH, expand=True, padx=10, pady=10)
ttk.Label(form_frame, text="Score(/10):", font=("Calibri 24 bold", 11)).grid(row=2, column=0,padx=10, pady=5, sticky="e")
 
 
 
window.mainloop()

