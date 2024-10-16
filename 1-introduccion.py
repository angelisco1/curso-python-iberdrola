# String
text = "Hola mundo!"
print(text)
print(type(text))

# Int
cantidad = 17
print(type(cantidad))

# Float
precio = 10.99
print(type(precio))

# Boolean (True o False)
hay_stock = True
print(type(hay_stock))

# None
es_null = None
print(type(es_null))

print(cantidad)
cantidad = cantidad - 1

ganancias_posibles = cantidad * precio
print(ganancias_posibles)

# Casting de tipos
print(int(ganancias_posibles))
print(str(ganancias_posibles))
print(float(8))

# Redondea el número
print(round(ganancias_posibles))

# Complex
print(2+5j + 1+2j)

# Verificación de tipos
print(isinstance(ganancias_posibles, float))
print(isinstance(ganancias_posibles, int))
print(round(8.294, 2))

# Formateo de strings
# Producto A: Stock (16), Posibles ganancias (175.84)
producto = "Producto A"
print(producto + ": Stock (" + str(cantidad) + "), Posibles ganancias (" + str(ganancias_posibles) + ")")
print("%s: Stock (%d), Posibles ganancias (%f)" % (producto, cantidad, ganancias_posibles))

# Nuevo formateador
print("{}: Stock ({}), Posibles ganancias ({})".format(producto, cantidad, ganancias_posibles))
# f-string
print(f"{producto}: Stock ({cantidad}), Posibles ganancias ({ganancias_posibles})")

# Listas
lista_de_varios_elementos = [1, "Hola mundo", 8.94, True]
print(lista_de_varios_elementos)

lista_productos = ["Patatas", "Aceite", "Sal", "Vinagre"]

print(lista_productos[3])

# Obtenemos la longitud
longitud_lista = len(lista_productos)
print(longitud_lista)
print(len(text))

lista_productos.append("Pimientos")
print(lista_productos)

# pop -> elimina de la lista el último elemento y lo devuelve
pimientos = lista_productos.pop()
# print(pimientos)
print(lista_productos)

# clear -> deja la lista vacía
lista_productos.clear()
print(lista_productos)

lista_de_varios_elementos = "pedro"
print(lista_de_varios_elementos)

lista_numeros = [1, 2, 3, 3, 3, 4, 4, 5, 6, 6, 7]
print(lista_numeros.count(3))
print(lista_numeros.count(6))
print(lista_numeros.index(5))

# Diccionario (Dict)
persona1 = {
  "nombre": "Charly",
  "apellidos": "Falco",
  "edad": 39,
  "direccion": "C/ Norte 9, Madrid",
  "dni": "00000000T",
  "esta_trabajando": True
}

persona2 = {
  "nombre": "Mike",
  "apellidos": "Kozinski",
  "edad": 41,
  "direccion": "C/ Norte 12, Madrid",
  "dni": "00000001S",
  "esta_trabajando": False
}

persona3 = {
  "nombre": "Octavia",
  "apellidos": "Blake",
  "edad": 30,
  "direccion": "C/ Este 2, Madrid",
  "dni": "00000003E",
  "esta_trabajando": True
}

# Opción 1
lista_usuarios = [persona1, persona2, persona3]
print(lista_usuarios)
# Opción 2
# lista_usuarios = []
# lista_usuarios.append(persona1)
# lista_usuarios.append(persona2)
# lista_usuarios.append(persona3)

print(type(persona1))
print(type(lista_usuarios))

# Bucle For
for persona in lista_usuarios:
  print(f"- {persona['nombre']} {persona['apellidos']}")

num_personas = len(lista_usuarios)
suma_edades = 0
for pers in lista_usuarios:
  suma_edades = suma_edades + pers["edad"]
  print(suma_edades)

media_edades = suma_edades / num_personas
print(f"La media de edad de las personas es: {media_edades}")

# for con enumerate: obtenemos la posición de los elementos
for persona in enumerate(lista_usuarios):
  # print(persona)
  # persona[0] -> 0, 1, 2
  # persona[1] -> {nombre: 'Charly', ...}, {nombre: 'Mike', ...}
  print(f"{persona[0] + 1}: {persona[1]['nombre']} - {persona[1]['dni']}")

# 1: Charly - 00000000T
# 2: Mike - 00000001S
# 3: Octavia - 00000003E

posicion = 0
for persona in lista_usuarios:
  posicion = posicion + 1
  print(f"{posicion}: {persona['nombre']} - {persona['dni']}")


# Condicional IF
if 2 > 0:
  print("El 2 es mayor que 0")

if 2 <= 0:
  print("El 2 es menor o igual que 0")

if 2 > 8:
  print("El 2 es mayor que 8")
else:
  print("El 2 es menor o igual que 8")

# Mostrar una lista con los usuarios que buscan trabajo
for persona in lista_usuarios:
  # if persona["esta_trabajando"] == False:
  if not persona["esta_trabajando"]:
    print(f"{persona['nombre']} está buscando trabajo")


# Unpacking - Desempaquetado
# for persona in enumerate(lista_usuarios):
#   print(f"{persona[0] + 1}: {persona[1]['nombre']} - {persona[1]['dni']}")
for posicion, persona in enumerate(lista_usuarios):
  print(f"{posicion + 1}: {persona['nombre']} - {persona['dni']}")

telefono = ("+34", 666777888, True, [], "texto")
prefijo = telefono[0]
numero = telefono[1]
print(prefijo)
print(numero)

prefijo, numero, *resto_datos, texto = telefono
print(prefijo)
print(numero)
print(resto_datos)
print(texto)

# telefono[0] = "+37"
# TypeError: 'tuple' object does not support item assignment

# Slicing
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista[-1])
print(lista[1:3])
print(lista[4:9])
print(lista[4:])
print(lista[0::2])
print(lista[1::2])
print(lista[::-2])
print(lista[-2::2])

# Muestra los números que están en las posiciones pares
lista_de_2_en_2 = []
for posicion, numero in enumerate(lista):
  if posicion % 2 == 0:
    lista_de_2_en_2.append(numero)

print(lista_de_2_en_2)

# Sets (conjuntos
lista_nums = [1, 2, 2, 2, 3, 4, 4, 5, 6, 7, 8, 1]
print(lista_nums)
print(set(lista_nums))

lista_passwords_inseguras = ['qwerty', '1234', 'password', '0000']
lista_passwords = ['qwerty', '1234', '322kofie2foifnd', 'password', '1234', 'asdkjakldj']
passwords_sin_repeticiones = set(lista_passwords)

print(passwords_sin_repeticiones.intersection(set(lista_passwords_inseguras)))
print(set(lista_passwords).intersection(set(lista_passwords_inseguras)))
print(passwords_sin_repeticiones.difference(set(lista_passwords_inseguras)))
print(passwords_sin_repeticiones.symmetric_difference(set(lista_passwords_inseguras)))

# Diccionarios
usuario = {
  "email": "cfalco@gmail.com",
  "password": "1234",
  "tipo": "premium"
}

if usuario["password"] == "1234" or usuario["password"] == "password":
  print("Ey, tienes que cambiar tu contraseña!")

if usuario["password"] in lista_passwords_inseguras:
  print("Ey, tienes que cambiar tu contraseña!")

print(usuario.values())
print(usuario.keys())
print(usuario.items())