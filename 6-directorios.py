import os

# Muestra la ruta actual
print(os.getcwd())

# Listar archivos y carpetas en una carpeta
with os.scandir("archivos/") as files:
  for file in files:
    print(f"{file.name} - {'Carpeta' if file.is_dir() else 'Archivo'}")

# Crear carpeta
with os.scandir("archivos/") as files:
  nombre_carpeta = "prueba2"
  if not nombre_carpeta in [file.name for file in files]:
    os.mkdir(f"archivos/{nombre_carpeta}")
    print("Se ha creado la carpeta.")
  else:
    print("La carpeta ya existe.")
