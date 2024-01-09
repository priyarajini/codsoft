import tkinter as tk

def on_button_click(value):
    current_text = entry_var.get()
    entry_var.set(current_text + str(value))

def clear_entry():
    entry_var.set("")

def calculate_result():
    try:
        result = eval(entry_var.get())
        entry_var.set(result)
    except Exception as e:
        entry_var.set("Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget for displaying the input and result
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=('Helvetica', 14), justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Define the buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Create and place buttons in the grid
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, padx=20, pady=20, font=('Helvetica', 14), command=lambda t=text: on_button_click(t) if t != '=' else calculate_result() if t != 'C' else clear_entry())
    button.grid(row=row, column=col)

# Start the main event loop
root.mainloop()
