import tkinter as tk
from tkinter import messagebox

def get_user_input():
    def on_submit():
        global user_input
        user_input = entry.get()
        root.destroy()

    root = tk.Tk()
    root.title("Introducir Números")
    root.geometry("400x200")

    label = tk.Label(root, text="Introduce números enteros positivos separados por comas:")
    label.pack(pady=10)

    entry = tk.Entry(root, width=50)
    entry.pack(pady=10)

    button = tk.Button(root, text="Enviar", command=on_submit)
    button.pack(pady=10)

    root.mainloop()
    return user_input

def process_input(values):
    try:
        # Convertir los valores de entrada en una lista de números enteros
        minterms = [int(x) for x in values.split(',')]
        # Ordenar la lista de números
        minterms.sort()
        return minterms
    except ValueError:
        messagebox.showerror("Error", "Por favor introduzca números enteros positivos separados por comas")
        return []

def generate_multiplexor(size, entry_list, selection_lines):
    root = tk.Tk()
    root.title("Multiplexor")
    
    # Ajustar el tamaño del canvas dinámicamente
    canvas_height = 100 + size * 30
    root.geometry("400x400")

    # Crear un frame para contener el canvas y el scrollbar
    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True)

    # Crear el canvas con un scrollbar vertical
    canvas = tk.Canvas(frame, width=400, height=400, highlightthickness=0)
    scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Crear un frame interno para el contenido del canvas
    content_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=content_frame, anchor="nw")

    # Limpiar el canvas antes de dibujar
    canvas.delete("all")
    
    # Calcular el número de entradas y líneas de selección
    num_inputs = size
    num_selection_lines = len(selection_lines)
    
    # Dibujar el cuerpo del multiplexor
    canvas.create_rectangle(100, 50, 450, 50 + num_inputs * 30, fill="lightgrey", outline="black")
    
    # Dibujar las entradas con números dentro del multiplexor
    for i in range(num_inputs):
        canvas.create_line(50, 70 + i*30, 100, 70 + i*30, fill="black")
        canvas.create_text(150, 70 + i*30, text=f"{i}", anchor="w")
        canvas.create_text(50, 70 + i*30, text=f"{entry_list[i]}", anchor="e")
    
    # Dibujar la salida
    canvas.create_line(450, 70 + (num_inputs * 30) // 2, 600, 70 + (num_inputs * 30) // 2, fill="black")
    canvas.create_text(510, 62 + (num_inputs * 30) // 2, text="Y", anchor="w")
    
    # Dibujar las líneas de selección con nombres
    for j, line in enumerate(selection_lines):
        canvas.create_line(200 + j*30, 50 + num_inputs * 30, 200 + j*30, 50 + num_inputs * 30 + 50, fill="black")
        canvas.create_text(200 + j*30, 50 + num_inputs * 30 + 60, text=line, anchor="n")

    content_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    root.mainloop()

def generate_mux(entry_list, control_vars):
    size = len(entry_list)
    generate_multiplexor(size, entry_list, control_vars)