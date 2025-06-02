import tkinter as tk
from tkinter import messagebox, font
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

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

def create_factorial_graph(n_max):
    x_vals = list(range(0, min(n_max + 1, 11)))  
    y_vals = [faktorial(x) for x in x_vals]
    return x_vals, y_vals, "Grafik Faktorial", "n", "n!"

def create_fibonacci_graph(n_max):
    x_vals = list(range(0, min(n_max + 1, 20)))  
    y_vals = [fibonacci(x) for x in x_vals]
    return x_vals, y_vals, "Grafik Fibonacci", "n", "F(n)"

def create_power_graph(x_base, n_max):
    x_vals = list(range(0, min(n_max + 1, 15)))  
    y_vals = [pangkat(x_base, n) for n in x_vals]
    return x_vals, y_vals, f"Grafik Pangkat (x={x_base})", "n", f"{x_base}^n"

def update_graph():
    try:
        ax.clear()
        
        n = int(entry_n["text"]) if entry_n["text"] else 5
        x = int(entry_x["text"]) if entry_x["text"] else 2
        operasi = var.get()
        
        n = min(n, 20)
        x = min(abs(x), 10) if x != 0 else 2
        
        if operasi == "Faktorial":
            x_vals, y_vals, title, xlabel, ylabel = create_factorial_graph(n)
       
            if n < len(x_vals):
                ax.scatter([n], [y_vals[n]], color='red', s=100, zorder=5, label=f'n={n}')
        elif operasi == "Fibonacci":
            x_vals, y_vals, title, xlabel, ylabel = create_fibonacci_graph(n)
          
            if n < len(x_vals):
                ax.scatter([n], [y_vals[n]], color='red', s=100, zorder=5, label=f'n={n}')
        elif operasi == "Pangkat":
            x_vals, y_vals, title, xlabel, ylabel = create_power_graph(x, n)
            
            if n < len(x_vals):
                ax.scatter([n], [y_vals[n]], color='red', s=100, zorder=5, label=f'n={n}')
        
 
        ax.plot(x_vals, y_vals, 'b-o', linewidth=2, markersize=4, alpha=0.7)
        ax.set_title(title, fontsize=12, fontweight='bold')
        ax.set_xlabel(xlabel, fontsize=10)
        ax.set_ylabel(ylabel, fontsize=10)
        ax.grid(True, alpha=0.3)
        ax.legend()
        
       
        ax.set_facecolor('#2a2a2a')
        fig.patch.set_facecolor('#1e1e1e')
        ax.tick_params(colors='white')
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.title.set_color('white')
        ax.spines['bottom'].set_color('white')
        ax.spines['top'].set_color('white')
        ax.spines['right'].set_color('white')
        ax.spines['left'].set_color('white')
        
  
        if max(y_vals) > 1000:
            ax.set_yscale('log')
            ax.set_ylabel(ylabel + ' (log scale)', fontsize=10)
        
        canvas.draw()
        
    except Exception as e:
        print(f"Error updating graph: {e}")


def tambah_digit(digit):
    global fokus_input
    if fokus_input == "n":
        entry_n.config(text=entry_n["text"] + digit)
    elif fokus_input == "x":
        entry_x.config(text=entry_x["text"] + digit)
    update_graph() 

def hapus_digit():
    global fokus_input
    if fokus_input == "n":
        entry_n.config(text=entry_n["text"][:-1])
    elif fokus_input == "x":
        entry_x.config(text=entry_x["text"][:-1])
    update_graph()  

def ganti_input():
    global fokus_input
    fokus_input = "x" if fokus_input == "n" else "n"
    label_fokus.config(text=f"Input aktif: {'n' if fokus_input == 'n' else 'x'}")

    
    entry_n.config(bg="#2e2e2e" if fokus_input == "n" else "#252525")
    entry_x.config(bg="#2e2e2e" if fokus_input == "x" else "#252525")

def on_operation_change():
    update_graph()  

def hitung():
    try:
        n = int(entry_n["text"]) if entry_n["text"] else 0
        x = int(entry_x["text"]) if entry_x["text"] else 0
        operasi = var.get()

        if operasi == "Faktorial":
            if n < 0:
                raise ValueError("Faktorial hanya untuk bilangan non-negatif")
            if n > 20:
                raise ValueError("Input terlalu besar untuk faktorial (maksimal 20)")
            hasil = faktorial(n)
        elif operasi == "Fibonacci":
            if n < 0:
                raise ValueError("Fibonacci hanya untuk bilangan non-negatif")
            if n > 35:
                raise ValueError("Input terlalu besar untuk fibonacci (maksimal 35)")
            hasil = fibonacci(n)
        elif operasi == "Pangkat":
            if abs(x) > 10 or n > 20:
                raise ValueError("Input terlalu besar untuk pangkat (x: -10 to 10, n: max 20)")
            hasil = pangkat(x, n)
        else:
            hasil = "Pilih operasi"

        label_hasil.config(text=f"Hasil: {hasil}")
        update_graph()  
    except ValueError as e:
        messagebox.showerror("Error", str(e) if str(e) else "Input tidak valid!")
    except RecursionError:
        messagebox.showerror("Error", "Input terlalu besar, terjadi recursion error!")

def on_resize(event):
    update_layout()

def update_layout():
    window_width = window.winfo_width()
    
    base_size = min(12, max(8, int(window_width / 80)))
    custom_font.configure(size=base_size)
    button_font.configure(size=base_size)
    title_font.configure(size=base_size + 2)
    result_font.configure(size=base_size + 1)

def make_cmd(c):
    return lambda: tambah_digit(c)


window = tk.Tk()
window.title("Kalkulator Rekursif dengan Visualisasi")
window.geometry("1000x800")
window.minsize(800, 600)


bg_color = "#1e1e1e"
fg_color = "#ffffff"
entry_color = "#2e2e2e"
button_color = "#3e3e3e"
highlight_color = "#4e4e4e"
active_color = "#5e5e5e"


custom_font = font.Font(family="Helvetica", size=10)
button_font = font.Font(family="Helvetica", size=10, weight="bold")
title_font = font.Font(family="Helvetica", size=12, weight="bold")
result_font = font.Font(family="Helvetica", size=11)

window.configure(bg=bg_color)


var = tk.StringVar(value="Faktorial")
fokus_input = "n"


main_frame = tk.Frame(window, bg=bg_color)
main_frame.pack(fill="both", expand=True, padx=10, pady=10)


left_panel = tk.Frame(main_frame, bg=bg_color, width=400)
left_panel.pack(side="left", fill="y", padx=(0, 10))
left_panel.pack_propagate(False)


right_panel = tk.Frame(main_frame, bg=bg_color)
right_panel.pack(side="right", fill="both", expand=True)



title_label = tk.Label(left_panel, text="Kalkulator Rekursif", bg=bg_color,
                       fg=fg_color, font=title_font, pady=10)
title_label.pack(fill="x")


operation_frame = tk.Frame(left_panel, bg=bg_color, pady=10)
operation_frame.pack(fill="x")

tk.Label(operation_frame, text="Pilih Operasi:", bg=bg_color, fg=fg_color,
         font=custom_font).pack(anchor="w", pady=(5, 10))

operations = [
    ("Faktorial (n!)", "Faktorial"),
    ("Fibonacci ke-n", "Fibonacci"),
    ("Pangkat (xⁿ)", "Pangkat")
]

for text, value in operations:
    rb = tk.Radiobutton(operation_frame, text=text, variable=var, value=value,
                        bg=bg_color, fg=fg_color, selectcolor=entry_color,
                        font=custom_font, padx=10, command=on_operation_change)
    rb.pack(anchor="w")


input_frame = tk.Frame(left_panel, bg=bg_color, pady=10)
input_frame.pack(fill="x")


input_n_frame = tk.Frame(input_frame, bg=bg_color)
input_n_frame.pack(fill="x", pady=5)
tk.Label(input_n_frame, text="Nilai n:", bg=bg_color, fg=fg_color,
         font=custom_font, width=12, anchor="w").pack(side=tk.LEFT)
entry_n = tk.Label(input_n_frame, text="", bg="#2e2e2e", fg=fg_color,
                   font=custom_font, width=15, anchor="e", padx=10, pady=5,
                   relief="sunken", bd=2)
entry_n.pack(side=tk.RIGHT, fill="x", expand=True)


input_x_frame = tk.Frame(input_frame, bg=bg_color)
input_x_frame.pack(fill="x", pady=5)
tk.Label(input_x_frame, text="Nilai x:", bg=bg_color, fg=fg_color,
         font=custom_font, width=12, anchor="w").pack(side=tk.LEFT)
entry_x = tk.Label(input_x_frame, text="", bg="#252525", fg=fg_color,
                   font=custom_font, width=15, anchor="e", padx=10, pady=5,
                   relief="sunken", bd=2)
entry_x.pack(side=tk.RIGHT, fill="x", expand=True)


label_fokus = tk.Label(left_panel, text="Input aktif: n", bg=bg_color,
                       fg="#aaaaaa", font=custom_font)
label_fokus.pack(pady=5)


button_frame = tk.Frame(left_panel, bg=bg_color, pady=10)
button_frame.pack()

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
            btn_text = "DEL"
        elif char == "⏎":
            cmd = ganti_input
            btn_text = "⟳"
        else:
            cmd = make_cmd(char)
            btn_text = char

        btn = tk.Button(num_pad, text=btn_text, command=cmd, width=3, height=1,
                        bg=button_color, fg=fg_color, font=button_font,
                        activebackground=active_color, activeforeground=fg_color,
                        relief="raised", bd=2)
        btn.grid(row=i, column=j, padx=3, pady=3, ipadx=8, ipady=8)


calculate_button = tk.Button(left_panel, text="Hitung", command=hitung,
                             bg=highlight_color, fg=fg_color, font=button_font,
                             activebackground=active_color, activeforeground=fg_color,
                             relief="raised", bd=2, padx=20, pady=10)
calculate_button.pack(pady=20)


label_hasil = tk.Label(left_panel, text="Hasil: ", bg=bg_color, fg=fg_color,
                       font=result_font, pady=10, wraplength=300)
label_hasil.pack()


graph_title = tk.Label(right_panel, text="Visualisasi Grafik", bg=bg_color,
                       fg=fg_color, font=title_font, pady=10)
graph_title.pack()


plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(6, 5), facecolor='#1e1e1e')
canvas = FigureCanvasTkAgg(fig, right_panel)
canvas.get_tk_widget().pack(fill="both", expand=True, padx=10, pady=10)


instructions = tk.Label(right_panel, 
                       text="• Grafik akan terupdate otomatis saat input berubah\n• Titik merah menunjukkan nilai saat ini\n• Skala logaritmik digunakan untuk nilai besar",
                       bg=bg_color, fg="#aaaaaa", font=("Helvetica", 9),
                       justify="left", padx=10)
instructions.pack(pady=(0, 10))


window.bind("<Configure>", on_resize)


update_graph()


window.mainloop()
