import tkinter as tk

def evaluate(event):
    result_var.set(eval(entry.get()))

app = tk.Tk()
app.title("Calculator")

entry = tk.Entry(app)
entry.pack()

entry.bind('<Return>', evaluate)

result_var = tk.StringVar()
result_label = tk.Label(app, textvariable=result_var)
result_label.pack()

app.mainloop()
