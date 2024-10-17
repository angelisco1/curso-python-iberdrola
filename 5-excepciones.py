from getpass import getpass

try:
  resultado = 1 / 'a'
  print(resultado)
except ZeroDivisionError as err:
  print('No es posible hacer esa división.')
  print(err)
except TypeError as err:
  print('No estás usando los tipos correctos.')
except Exception as err:
# except:
  print('Algo malo ha pasado')
  print(err)

print('Eeeee')

class InvalidCredentials(Exception):
  def __init__(self):
    super().__init__("Las credencias introducidas no son correctas.")


def validar_usuario(nombre, password):
  usuarios_registrados = [
    { "nombre": "angel", "password": "1234" },
    { "nombre": "mike", "password": "password" },
  ]

  usuario_valido = False
  for usuario in usuarios_registrados:
    if nombre == usuario["nombre"] and password == usuario["password"]:
      usuario_valido = True

  if not usuario_valido:
    # raise Exception("Las credenciales no son correctas")
    raise InvalidCredentials()


datos_incorrectos = True
while datos_incorrectos:
  # Input de datos
  nombre = input("Introduce tu nombre: ")
  password = getpass("Introduce tu contraseña: ")
  try:
    validar_usuario(nombre, password)
    print(f"Bienvenido {nombre} ({password})")
    datos_incorrectos = False
  except InvalidCredentials as err:
    print(err)
    print("Intentalo otra vez")
