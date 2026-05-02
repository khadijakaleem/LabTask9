import tkinter as tk
import math

def calculate(op):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if op == "Add":
            result = num1 + num2
        elif op == "Subtract":
            result = num1 - num2
        elif op == "Multiply":
            result = num1 * num2
        elif op == "Divide":
            if num2 == 0:
                result_label.config(text="Error: Division by zero")
                return
            result = num1 / num2

        result_label.config(text=f"Result: {result}")

    except ValueError:
        result_label.config(text="Error: Enter valid numbers")

def calculate_single(op):
    try:
        num1 = float(entry1.get())

        if op == "Square":
            result = num1 ** 2
        elif op == "Square Root":
            if num1 < 0:
                result_label.config(text="Error: Negative number")
                return
            result = math.sqrt(num1)

        result_label.config(text=f"Result: {result}")

    except ValueError:
        result_label.config(text="Error: Enter valid number")

# ── Window Setup ──────────────────────────────────────
root = tk.Tk()
root.title("GUI Calculator")
root.geometry("400x320")
root.resizable(False, False)

# ── Input Fields ──────────────────────────────────────
tk.Label(root, text="Enter First Number:").pack(pady=(15, 0))
entry1 = tk.Entry(root, width=20, font=("Arial", 12))
entry1.pack(pady=5)

tk.Label(root, text="Enter Second Number:").pack()
entry2 = tk.Entry(root, width=20, font=("Arial", 12))
entry2.pack(pady=5)

# ── Buttons Row 1 (Basic Operations) ─────────────────
btn_frame1 = tk.Frame(root)
btn_frame1.pack(pady=5)

for op in ["Add", "Subtract", "Multiply", "Divide"]:
    tk.Button(
        btn_frame1,
        text=op,
        width=8,
        font=("Arial", 10),
        command=lambda o=op: calculate(o)
    ).pack(side=tk.LEFT, padx=4)

# ── Buttons Row 2 (Square & Square Root) ─────────────
btn_frame2 = tk.Frame(root)
btn_frame2.pack(pady=5)

for op in ["Square", "Square Root"]:
    tk.Button(
        btn_frame2,
        text=op,
        width=12,
        font=("Arial", 10),
        bg="lightblue",
        command=lambda o=op: calculate_single(o)
    ).pack(side=tk.LEFT, padx=4)

tk.Label(btn_frame2, text="  (uses First Number only)", font=("Arial", 8), fg="gray").pack(side=tk.LEFT)

# ── Result Display ────────────────────────────────────
result_label = tk.Label(root, text="Result: ", font=("Arial", 13, "bold"))
result_label.pack(pady=10)

root.mainloop()