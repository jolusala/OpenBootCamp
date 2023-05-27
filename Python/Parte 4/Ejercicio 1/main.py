f  = open("archivo.txt", "w")
f.write("Hola mundo\n")
f.close()

f = open("archivo.txt", "r+")
print(f.read())
f.write(str(12345))
f.close()