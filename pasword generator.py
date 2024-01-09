import tkinter as tk
from tkinter import StringVar
import random
import string

def generate_password():
    length = int(length_var.get())
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for i in range(length))
    result_var.set(password)


window = tk.Tk()
window.title("Password Generator")


length_var = StringVar()
length_var.set(12)  

result_var = StringVar()


length_label = tk.Label(window, text="Password Length:")
length_entry = tk.Entry(window, textvariable=length_var, width=5)
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
result_label = tk.Label(window, text="Generated Password:")
result_entry = tk.Entry(window, textvariable=result_var, state='readonly', width=30)


length_label.grid(row=0, column=0, padx=10, pady=10)
length_entry.grid(row=0, column=1, padx=10, pady=10)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)
result_label.grid(row=2, column=0, padx=10, pady=10)
result_entry.grid(row=2, column=1, padx=10, pady=10)


window.mainloop()
