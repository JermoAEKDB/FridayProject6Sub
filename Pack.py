import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def perform_operation(operation):
    global f_num
    global math_operation
    f_num = float(entry.get())
    math_operation = operation
    entry.delete(0, tk.END)

def button_equal():
    second_number = float(entry.get())
    entry.delete(0, tk.END)
    if math_operation == "addition":
        result = f_num + second_number
    elif math_operation == "subtraction":
        result = f_num - second_number
    elif math_operation == "multiplication":
        result = f_num * second_number
    elif math_operation == "division":
        result = f_num / second_number
    entry.insert(0, result)

def toggle_entry_state():
    entry.config(state=tk.NORMAL if entry["state"] == "disabled" else tk.DISABLED)
    toggle_button.config(text="Disable Entry" if entry["state"] == "normal" else "Enable Entry")

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=35, borderwidth=5, state="disabled")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2),
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2),
    ("0", 4, 0), ("+", 5, 0), ("=", 5, 1),
    ("-", 4, 1), ("*", 4, 2), ("/", 5, 2),
    ("Clear", 4, 1),
]

for (text, row, column) in buttons:
    button = tk.Button(root, text=text, padx=40, pady=20,
                       command=lambda t=text: button_click(t) if t.isdigit() else
                       button_clear() if t == "Clear" else perform_operation(t))
    button.grid(row=row, column=column)

toggle_button = tk.Button(root, text="Enable Entry", padx=20, pady=20, command=toggle_entry_state)
toggle_button.grid(row=6, column=0, columnspan=4)

root.mainloop()
