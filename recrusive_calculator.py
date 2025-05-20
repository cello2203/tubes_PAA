import tkinter as tk
from tkinter import messagebox, font



def faktorial(n):
    if n == 0 or n == 1:
        return 1
    return n * faktorial(n - 1)


def pangkat(x, n):
    if n == 0:
        return 1
    return x * pangkat(x, n - 1)


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)



def tambah_digit(digit):
    global fokus_input
    if fokus_input == "n":
        entry_n.config(text=entry_n["text"] + digit)
    elif fokus_input == "x":
        entry_x.config(text=entry_x["text"] + digit)


def hapus_digit():
    global fokus_input
    if fokus_input == "n":
        entry_n.config(text=entry_n["text"][:-1])
    elif fokus_input == "x":
        entry_x.config(text=entry_x["text"][:-1])


def ganti_input():
    global fokus_input
    fokus_input = "x" if fokus_input == "n" else "n"
    label_fokus.config(text=f"Input aktif: {'n' if fokus_input == 'n' else 'x'}")


    entry_n.config(bg="#2e2e2e" if fokus_input == "n" else "#252525")
    entry_x.config(bg="#2e2e2e" if fokus_input == "x" else "#252525")


def hitung():
    try:
        n = int(entry_n["text"]) if entry_n["text"] else 0
        x = int(entry_x["text"]) if entry_x["text"] else 0
        operasi = var.get()

        if operasi == "Faktorial":
            if n < 0:
                raise ValueError("Faktorial hanya untuk bilangan non-negatif")
            hasil = faktorial(n)
        elif operasi == "Fibonacci":
            if n < 0:
                raise ValueError("Fibonacci hanya untuk bilangan non-negatif")
            hasil = fibonacci(n)
        elif operasi == "Pangkat":
            hasil = pangkat(x, n)
        else:
            hasil = "Pilih operasi"

        label_hasil.config(text=f"Hasil: {hasil}")
    except ValueError as e:
        messagebox.showerror("Error", str(e) if str(e) else "Input tidak valid!")
    except RecursionError:
        messagebox.showerror("Error", "Input terlalu besar, terjadi recursion error!")


def on_resize(event):

    update_layout()


def update_layout():

    window_width = window.winfo_width()
    window_height = window.winfo_height()


    center_frame.place(relx=0.5, rely=0.5, anchor="center")


    min_width = 300
    min_height = 400
    width = max(min_width, int(window_width * 0.8))
    height = max(min_height, int(window_height * 0.8))


    base_size = min(12, max(8, int(window_width / 50)))
    custom_font.configure(size=base_size)
    button_font.configure(size=base_size)
    title_font.configure(size=base_size + 2)
    result_font.configure(size=base_size + 1)



window = tk.Tk()
window.title("Kalkulator Rekursif")

# Set initial window size with minimum dimensions
window.geometry("600x600")
window.minsize(400, 500)

# Colors
bg_color = "#1e1e1e"
fg_color = "#ffffff"
entry_color = "#2e2e2e"
button_color = "#3e3e3e"
highlight_color = "#4e4e4e"
active_color = "#5e5e5e"

# Create custom fonts that can be dynamically resized
custom_font = font.Font(family="Helvetica", size=12)
button_font = font.Font(family="Helvetica", size=12, weight="bold")
title_font = font.Font(family="Helvetica", size=14, weight="bold")
result_font = font.Font(family="Helvetica", size=13)

# Configure the window
window.configure(bg=bg_color)

# --- Variables ---
var = tk.StringVar(value="Faktorial")
fokus_input = "n"  # Default active input is 'n'

# Create a main frame to center everything
center_frame = tk.Frame(window, bg=bg_color, padx=20, pady=20)

# Title
title_label = tk.Label(center_frame, text="Kalkulator Rekursif", bg=bg_color,
                       fg=fg_color, font=title_font, pady=10)
title_label.pack(fill="x")

# Operation selection frame
operation_frame = tk.Frame(center_frame, bg=bg_color, pady=10)
operation_frame.pack(fill="x")

tk.Label(operation_frame, text="Pilih Operasi:", bg=bg_color, fg=fg_color,
         font=custom_font).pack(anchor="w", pady=(5, 10))

operations = [
    ("Faktorial (n!)", "Faktorial"),
    ("Fibonacci ke-n", "Fibonacci"),
    ("Pangkat (xⁿ)", "Pangkat")
]

for text, value in operations:
    tk.Radiobutton(operation_frame, text=text, variable=var, value=value,
                   bg=bg_color, fg=fg_color, selectcolor=entry_color,
                   font=custom_font, padx=10).pack(anchor="w")

# Input frame
input_frame = tk.Frame(center_frame, bg=bg_color, pady=10)
input_frame.pack(fill="x")

# Input n
input_n_frame = tk.Frame(input_frame, bg=bg_color)
input_n_frame.pack(fill="x", pady=5)
tk.Label(input_n_frame, text="Nilai n:", bg=bg_color, fg=fg_color,
         font=custom_font, width=12, anchor="w").pack(side=tk.LEFT)
entry_n = tk.Label(input_n_frame, text="", bg="#2e2e2e", fg=fg_color,
                   font=custom_font, width=20, anchor="e", padx=10, pady=5)
entry_n.pack(side=tk.RIGHT, fill="x", expand=True)

# Input x
input_x_frame = tk.Frame(input_frame, bg=bg_color)
input_x_frame.pack(fill="x", pady=5)
tk.Label(input_x_frame, text="Nilai x (untuk xⁿ):", bg=bg_color, fg=fg_color,
         font=custom_font, width=12, anchor="w").pack(side=tk.LEFT)
entry_x = tk.Label(input_x_frame, text="", bg="#252525", fg=fg_color,
                   font=custom_font, width=20, anchor="e", padx=10, pady=5)
entry_x.pack(side=tk.RIGHT, fill="x", expand=True)

# Active input indicator
label_fokus = tk.Label(center_frame, text="Input aktif: n", bg=bg_color,
                       fg="#aaaaaa", font=custom_font)
label_fokus.pack(pady=5)

# Number buttons frame
button_frame = tk.Frame(center_frame, bg=bg_color, pady=10)
button_frame.pack()

# Create numeric keypad
num_pad = tk.Frame(button_frame, bg=bg_color)
num_pad.pack()

buttons = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"],
    ["↺", "0", "⏎"]
]

for i, row in enumerate(buttons):
    for j, char in enumerate(row):
        if char == "↺":
            cmd = hapus_digit
            btn_text = "⌫"  # Backspace symbol
        elif char == "⏎":
            cmd = ganti_input
            btn_text = "⟳"  # Switch symbol
        else:
            cmd = lambda c=char: tambah_digit(c)
            btn_text = char

        btn = tk.Button(num_pad, text=btn_text, command=cmd, width=3, height=1,
                        bg=button_color, fg=fg_color, font=button_font,
                        activebackground=active_color, activeforeground=fg_color,
                        relief="raised", bd=2)
        btn.grid(row=i, column=j, padx=5, pady=5, ipadx=10, ipady=10)

# Calculate button
calculate_button = tk.Button(center_frame, text="Hitung", command=hitung,
                             bg=highlight_color, fg=fg_color, font=button_font,
                             activebackground=active_color, activeforeground=fg_color,
                             relief="raised", bd=2, padx=20, pady=10)
calculate_button.pack(pady=20)

# Result display
label_hasil = tk.Label(center_frame, text="Hasil: ", bg=bg_color, fg=fg_color,
                       font=result_font, pady=10)
label_hasil.pack()

# Bind resize event to update layout
window.bind("<Configure>", on_resize)

# Initial layout update
window.update_idletasks()
update_layout()

# Run the GUI
window.mainloop()
