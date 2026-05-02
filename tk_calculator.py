import tkinter as tk

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

# ── Window Setup ──────────────────────────────────────
root = tk.Tk()
root.title("GUI Calculator")
#root.geometry("300x280")
root.geometry("400x280")
root.resizable(False, False)

# ── Input Fields ──────────────────────────────────────
tk.Label(root, text="Enter First Number:").pack(pady=(15, 0))
entry1 = tk.Entry(root, width=20, font=("Arial", 12))
entry1.pack(pady=5)

tk.Label(root, text="Enter Second Number:").pack()
entry2 = tk.Entry(root, width=20, font=("Arial", 12))
entry2.pack(pady=5)

# ── Buttons ───────────────────────────────────────────
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

for op in ["Add", "Subtract", "Multiply", "Divide"]:
    tk.Button(
        btn_frame,
        text=op,
        width=10,
        font=("Arial", 10),
        command=lambda o=op: calculate(o)
    ).pack(side=tk.LEFT, padx=4)

# ── Result Display ────────────────────────────────────
result_label = tk.Label(root, text="Result: ", font=("Arial", 13, "bold"))
result_label.pack(pady=10)

root.mainloop()