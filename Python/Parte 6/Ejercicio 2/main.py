import tkinter as tk

def mostrar_seleccion():
    seleccion = listbox.curselection()
    if seleccion:
        indice = seleccion[0]
        texto_seleccionado = opciones[indice]
        label.config(text=texto_seleccionado)

# Lista de opciones
opciones = ["Opción 1", "Opción 2", "Opción 3"]

# Crear ventana principal
ventana = tk.Tk()

# Label
label = tk.Label(ventana, text="Selecciona una opción")
label.pack()

# Lista de elementos seleccionables
listbox = tk.Listbox(ventana)
for opcion in opciones:
    listbox.insert(tk.END, opcion)
listbox.pack()

# Botón de mostrar selección
mostrar_button = tk.Button(ventana, text="Mostrar selección", command=mostrar_seleccion)
mostrar_button.pack()

# Mostrar ventana
ventana.mainloop()
