import tkinter as tk


def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))


def clear():
    entry.delete(0, tk.END)


def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


root = tk.Tk()
root.title("Simple Calculator")
root.geometry("320x450")
root.resizable(False, False)


entry = tk.Entry(root, font=("Arial", 20), bd=10, relief="ridge", justify="right")
entry.pack(fill="both", padx=10, pady=10)


buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+'],
    ['C']
]


for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")

    for button in row:
        if button == "=":
            cmd = calculate
        elif button == "C":
            cmd = clear
        else:
            cmd = lambda x=button: click(x)

        tk.Button(
            frame,
            text=button,
            font=("Arial", 18),
            command=cmd
        ).pack(side="left", expand=True, fill="both", padx=2, pady=2)


root.mainloop()