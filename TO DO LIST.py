import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_task = listbox.curselection()
    if selected_task:
        listbox.delete(selected_task)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Entry widget for entering tasks
entry = tk.Entry(root, font=('Helvetica', 14))
entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2, sticky="ew")

# Button to add a task
add_button = tk.Button(root, text="Add", font=('Helvetica', 12), command=add_task)
add_button.grid(row=0, column=2, padx=10, pady=10, sticky="ew")

# Listbox to display tasks
listbox = tk.Listbox(root, font=('Helvetica', 14), selectmode=tk.SINGLE)
listbox.grid(row=1, column=0, padx=10, pady=10, columnspan=2, sticky="nsew")

# Scrollbar for the listbox
scrollbar = tk.Scrollbar(root, command=listbox.yview)
scrollbar.grid(row=1, column=2, pady=10, sticky="nsew")
listbox.config(yscrollcommand=scrollbar.set)

# Button to remove a selected task
remove_button = tk.Button(root, text="Remove", font=('Helvetica', 12), command=remove_task)
remove_button.grid(row=2, column=0, columnspan=3, pady=10, sticky="ew")

# Configure row and column weights for resizing
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

# Start the main event loop
root.mainloop()
