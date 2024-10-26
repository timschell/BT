import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Simple Calculator")

        self.result_var = tk.StringVar()

        self.entry = tk.Entry(master, textvariable=self.result_var, justify='right', font=('Arial', 18))
        self.entry.grid(row=0, column=0, columnspan=4)

        self.create_buttons()

    def create_buttons(self):
        button_texts = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        for i, text in enumerate(button_texts):
            button = tk.Button(self.master, text=text, width=5, height=2, font=('Arial', 18),
                               command=lambda txt=text: self.on_button_click(txt))
            button.grid(row=1 + i // 4, column=i % 4)

        clear_button = tk.Button(self.master, text='C', width=22, height=2, font=('Arial', 18),
                                 command=self.clear)
        clear_button.grid(row=5, column=0, columnspan=4)

    def on_button_click(self, char):
        if char == '=':
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except Exception as e:
                messagebox.showerror("Error", f"Invalid operation: {e}")
        else:
            current_text = self.result_var.get()
            new_text = current_text + char
            self.result_var.set(new_text)

    def clear(self):
        self.result_var.set('')


def main():
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
