import sqlite3

# Conexión a la base de datos
conexion = sqlite3.connect('alumnos.db')

# Crear cursor
cursor = conexion.cursor()

# Crear tabla Alumnos
cursor.execute('''CREATE TABLE Alumnos
                  (id INTEGER, nombre TEXT, apellido TEXT)''')

# Insertar datos en la tabla
datos_alumnos = [
    (1, "Juan", "González"),
    (2, "María", "López"),
    (3, "Pedro", "Martínez"),
    (4, "Laura", "Pérez"),
    (5, "Carlos", "Rodríguez"),
    (6, "Ana", "Sánchez"),
    (7, "David", "Gómez"),
    (8, "Isabel", "Torres")
]

cursor.executemany('INSERT INTO Alumnos VALUES (?,?,?)', datos_alumnos)

# Guardar cambios
conexion.commit()

# Búsqueda de un alumno por nombre
nombre_buscar = "María"
cursor.execute("SELECT * FROM Alumnos WHERE nombre=?", (nombre_buscar,))
alumno_encontrado = cursor.fetchone()

if alumno_encontrado:
    print("Alumno encontrado:")
    print("ID:", alumno_encontrado[0])
    print("Nombre:", alumno_encontrado[1])
    print("Apellido:", alumno_encontrado[2])
else:
    print("Alumno no encontrado")

# Cerrar conexión
conexion.close()
