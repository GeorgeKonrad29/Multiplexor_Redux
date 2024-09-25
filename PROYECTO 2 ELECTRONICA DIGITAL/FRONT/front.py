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
    canvas_height = 150 + size * 30
    root.geometry(f"400x{canvas_height}")

    canvas = tk.Canvas(root, width=400, height=canvas_height, highlightthickness=0)
    canvas.pack(pady=10)

    # Limpiar el canvas antes de dibujar
    canvas.delete("all")
    
    # Calcular el número de entradas y líneas de selección
    num_inputs = size
    num_selection_lines = len(selection_lines)
    
    # Dibujar el cuerpo del multiplexor
    canvas.create_rectangle(100, 50, 300, 50 + num_inputs * 30, fill="lightgrey", outline="black")
    
    # Dibujar las entradas con números dentro del multiplexor
    for i in range(num_inputs):
        canvas.create_line(50, 70 + i*30, 100, 70 + i*30, fill="black")
        canvas.create_text(150, 70 + i*30, text=f"{i}", anchor="w")
        canvas.create_text(50, 70 + i*30, text=f"{entry_list[i]}", anchor="e")
    
    # Dibujar la salida
    canvas.create_line(300, 70 + (num_inputs * 30) // 2, 350, 70 + (num_inputs * 30) // 2, fill="black")
    canvas.create_text(360, 70 + (num_inputs * 30) // 2, text="Y", anchor="w")
    
    # Dibujar las líneas de selección con nombres
    for j, line in enumerate(selection_lines):
        canvas.create_line(200 + j*30, 50 + num_inputs * 30, 200 + j*30, 50 + num_inputs * 30 + 50, fill="black")
        canvas.create_text(200 + j*30, 50 + num_inputs * 30 + 60, text=line, anchor="n")

    root.mainloop()

def generate_mux(entry_list, control_vars):
    size = len(entry_list)
    generate_multiplexor(size, entry_list, control_vars)

if __name__ == "__main__":
    user_input = get_user_input()
    minterms = process_input(user_input)
    