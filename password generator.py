import tkinter as tk
from tkinter import StringVar
import random
import string

def generate_password():
    length = int(length_var.get())
    if length <= 0:
        result_var.set("Invalid length")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    result_var.set(password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Length entry and label
length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, pady=10)

length_var = StringVar()
length_entry = tk.Entry(root, textvariable=length_var, width=5)
length_entry.grid(row=0, column=1, pady=10)

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=0, column=2, pady=10)

# Result label
result_var = StringVar()
result_label = tk.Label(root, textvariable=result_var, font=('Helvetica', 12))
result_label.grid(row=1, column=0, columnspan=3, pady=10)

# Start the main event loop
root.mainloop()
