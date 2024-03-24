import tkinter as tk

class CalculatorApp:
    def __init__(self, master):
        self.equation = ""
        
        # Entry box
        self.entry = tk.Text(master, state='disabled', height=2, width=30)
        self.entry.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Buttons
        button_frame = tk.Frame(master)
        button_frame.pack()
        
        numbers = [
            '7', '8', '9',
            '4', '5', '6',
            '1', '2', '3',
            '0', '.', '='
        ]
        
        for num in numbers:
            tk.Button(button_frame, text=num, command=lambda char=num: self.on_button_click(char)).grid(row=(numbers.index(num)//3), column=(numbers.index(num)%3), padx=5, pady=5)
        
        operations = [
            '/', '*', '-', '+', 'C'
        ]
        
        for operation in operations:
            tk.Button(button_frame, text=operation, command=lambda char=operation: self.on_button_click(char)).grid(row=(operations.index(operation)//2), column=(numbers.index(num)%3 + 1), padx=5, pady=5)

    def on_button_click(self, char):
        if char == '=':
            result = self.calculate()
            self.clear_entry()
            self.entry.insert(tk.END, result)
        elif char == 'C':
            self.clear_entry()
        else:
            self.equation += char
            self.entry.config(state='normal')
            self.entry.insert(tk.END, char)

    def calculate(self):
        try:
            result = str(eval(self.equation))
            self.equation = result
            return result
        except:
            return "Error"

    def clear_entry(self):
        self.equation = ''
        self.entry.config(state='normal')
        self.entry.delete('1.0', tk.END)
        self.entry.config(state='disabled')

def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
