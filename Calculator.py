import tkinter as tk
from tkinter import messagebox

def calculate(op):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result = num1 / num2

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")
    except ZeroDivisionError as e:
        messagebox.showerror("Math Error", str(e))

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x280")
root.resizable(False, False)

tk.Label(root, text="Enter first number:").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter second number:").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack()

tk.Label(root, text="Choose Operation:").pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack()

tk.Button(button_frame, text="+", width=5, command=lambda: calculate('+')).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="-", width=5, command=lambda: calculate('-')).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="*", width=5, command=lambda: calculate('*')).grid(row=0, column=2, padx=5)
tk.Button(button_frame, text="/", width=5, command=lambda: calculate('/')).grid(row=0, column=3, padx=5)

result_label = tk.Label(root, text="Result: ", font=("Arial", 12))
result_label.pack(pady=20)

root.mainloop()