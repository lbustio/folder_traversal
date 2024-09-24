import os

def listar_directorio(directorio, nivel=0):
    esquema = ""
    for nombre in os.listdir(directorio):
        ruta_completa = os.path.join(directorio, nombre)
        esquema += "  " * nivel + "- " + nombre + "\n"
        if os.path.isdir(ruta_completa):
            esquema += listar_directorio(ruta_completa, nivel + 1)
    return esquema

ruta_base = r"D:\cloud\OneDrive - Universidad Iberoamericana, A.C\Escritorio\ml-project-name"
esquema = listar_directorio(ruta_base)

print(esquema)

# Guardar el esquema en un archivo de texto
with open("esquema_directorio.txt", "w", encoding="utf-8") as archivo:
    archivo.write(esquema)

print("Esquema generado y guardado en 'esquema_directorio.txt'.")
