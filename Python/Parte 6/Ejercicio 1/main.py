import tkinter as tk

def reiniciar_seleccion():
    for radio_button in radio_buttons:
        radio_button.deselect()

def mostrar_seleccion():
    for i, radio_button in enumerate(radio_buttons):
        if radio_button.get() == 1:
            print(f"Opción seleccionada: {opciones[i]}")

# Lista de opciones
opciones = ["Opción 1", "Opción 2", "Opción 3"]

# Crear ventana principal
ventana = tk.Tk()

# Variables para guardar el estado de los RadioButtons
radio_var = tk.IntVar()

# Lista para almacenar los RadioButtons
radio_buttons = []

# Crear los RadioButtons y mostrar las opciones
for opcion in opciones:
    radio_button = tk.Radiobutton(ventana, text=opcion, variable=radio_var, value=len(radio_buttons))
    radio_button.pack()
    radio_buttons.append(radio_button)

# Botón de reinicio
reiniciar_button = tk.Button(ventana, text="Reiniciar", command=reiniciar_seleccion)
reiniciar_button.pack()

# Botón de mostrar selección
mostrar_button = tk.Button(ventana, text="Mostrar selección", command=mostrar_seleccion)
mostrar_button.pack()

# Mostrar ventana
ventana.mainloop()
