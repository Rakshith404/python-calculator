import tkinter as tk

# ---------------- CONFIG ----------------
MAX_DISPLAY_CHARS = 12
BTN_ACTIVE_BG = "#d0d0d0"
BTN_NORMAL_BG = "#f2f2f2"

# ---------------- APP ----------------
root = tk.Tk()
root.title("Calculator")
root.geometry("300x420")
root.resizable(False, False)

expression = ""

# ---------------- FUNCTIONS ----------------
def format_number(value):
    try:
        value = float(value)
        if abs(value) >= 10 ** MAX_DISPLAY_CHARS:
            return f"{value:.6e}".replace("e", "×10^")
        return str(value)[:MAX_DISPLAY_CHARS]
    except:
        return value


def update_display(value):
    display_var.set(value)


def press(key):
    global expression

    if key == "C":
        expression = ""
        update_display("")
        return

    if key == "Back":
        expression = expression[:-1]
        update_display(expression)
        return

    if key == "=":
        try:
            result = eval(expression)
            expression = format_number(result)
            update_display(expression)
        except:
            update_display("Error")
            expression = ""
        return

    if key in "+-*/":
        if expression and expression[-1] not in "+-*/":
            expression += key
            update_display(expression)
        return

    if len(expression.replace(".", "").replace("+", "").replace("-", "").replace("*", "").replace("/", "")) < MAX_DISPLAY_CHARS:
        expression += key
        update_display(expression)
    else:
        try:
            value = eval(expression + key)
            expression = format_number(value)
            update_display(expression)
        except:
            pass


def animate(btn):
    btn.config(bg=BTN_ACTIVE_BG)
    root.after(80, lambda: btn.config(bg=BTN_NORMAL_BG))


def on_button_click(key, btn):
    animate(btn)
    press(key)


# ---------------- KEYBOARD ----------------
def keyboard_input(event):
    if event.char in "0123456789+-*/.":
        press(event.char)
    elif event.keysym == "Return":
        press("=")
    elif event.keysym == "BackSpace":
        press("Back")
    elif event.keysym == "Escape":
        press("C")


root.bind("<Key>", keyboard_input)

# ---------------- DISPLAY ----------------
display_var = tk.StringVar()

display = tk.Entry(
    root,
    textvariable=display_var,
    font=("Segoe UI", 18),
    bd=6,
    relief="sunken",
    justify="right"
)

display.place(x=10, y=15, width=280, height=70)

# ---------------- BUTTONS ----------------
buttons = [
    ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
    (".", 3, 0), ("0", 3, 1), ("Back", 3, 2), ("+", 3, 3),
    ("C", 4, 0), ("=", 4, 2),
]

frame = tk.Frame(root)
frame.place(relx=0.5, y=90, anchor="n")

for text, row, col in buttons:
    btn = tk.Button(
        frame,
        text=text,
        font=("Segoe UI", 12),
        width=5 if text not in ("C", "=") else 11,
        height=2,
        bg=BTN_NORMAL_BG
    )
    btn.grid(
        row=row,
        column=col,
        padx=3,
        pady=3,
        columnspan=2 if text in ("C", "=") else 1
    )
    btn.config(command=lambda t=text, b=btn: on_button_click(t, b))

# ---------------- RUN ----------------
root.mainloop()
