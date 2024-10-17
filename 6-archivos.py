# file = open("archivos/passwords-filtradas.txt", "r")
# contenido = file.read()
# print(contenido)
# file.close()

with open("archivos/passwords-filtradas.txt", "r") as file:
  contenido = file.read()
  print(contenido)

with open("archivos/passwords-filtradas.txt", "r") as file:
  linea1 = file.readline()
  print(linea1.strip())
  linea2 = file.readline()
  print(linea2.strip())

# with open("archivos/passwords-filtradas.txt", "r") as file:
#   while linea := file.readline():
#     print(linea.strip())
#     input('Intro para seguir')

usuarios_registrados = [
  { "nombre": "angel", "password": "asdasdsafasf" },
  { "nombre": "mike", "password": "password" },
]

def avisar_cambiar_contraseña(usuarios):
  with open("archivos/passwords-filtradas.txt", "r") as file:
    # contraseñas = file.read().split("\n")
    contraseñas = [linea.strip() for linea in file.readlines()]
    print(contraseñas)
    for usuario in usuarios:
      if usuario["password"] in contraseñas:
        print(f"El usuario {usuario['nombre']} tiene que cambiar la contraseña")

avisar_cambiar_contraseña(usuarios_registrados)

def avisar_cambiar_contraseñas2(usuarios):
  with open("archivos/passwords-filtradas.txt", "r") as file:
    while linea := file.readline():
      for usuario in usuarios:
        if usuario["password"] == linea.strip():
          print(f"El usuario {usuario['nombre']} tiene que cambiar la contraseña")

avisar_cambiar_contraseñas2(usuarios_registrados)

# Escritura de archivos
with open("archivos/chat.txt", "w", encoding="utf-8") as file:
  file.write("+ Hola, ¿qué tal?\n")
  file.write("- Muy bien, y tu?\n")

# Añadir contenido a los archivos
with open("archivos/passwords-filtradas.txt", "a") as file:
  file.write("\n0000")