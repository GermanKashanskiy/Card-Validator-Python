import re
import tkinter as tk
from tkinter import ttk

def is_valid(newval):
    card_visa = r"^[4][5][8][0][0-9]{0,12}$"
    card_masterc = r"^[5][0-9]{0,15}$"
    valid_visa = re.match(card_visa, newval)
    valid_masterc = re.match(card_masterc, newval)
    if valid_visa:
        label["text"] = "Your card is VISA"
    elif valid_masterc:
        label["text"] = "Your card is Master Card"
    else:
        label["text"] = "We dont support this card"

root = tk.Tk()
root.title("Card Validator")
root.geometry("250x200")

errmsg = tk.StringVar()

entry = ttk.Entry()
entry.pack(padx=5, pady=5, anchor=tk.NW)

btn = ttk.Button(text="Click Me", command=lambda: is_valid(entry.get()))
btn.pack()

label = ttk.Label()
label.pack(padx=5, pady=5, anchor=tk.NW)

root.mainloop()
