def nombre_funcion():
  pass

def suma(n1, n2):
  # s = n1 + n2
  # print(s)
  # return s
  return n1 + n2

s1 = suma(1, 2)
s2 = suma(2, 5)
suma(102, 55)
print(s1+s2)
print(suma(s1, s2))

# Función con parámetro por defecto
def saludar(nombre="Mundo"):
  return f"Hola {nombre}"

print(saludar("Javi"))
print(saludar())

# *args
# def get_ticket_loteria(sorteo, *args):
def get_ticket_loteria(sorteo, *numeros):
  numeros_str = []
  # for num in args:
  for num in numeros:
    numeros_str.append(str(num))
    numeros_unidos = ', '.join(numeros_str)
  print(f"Sorteo: {sorteo}. Los números elegidos son: {numeros_unidos}")

get_ticket_loteria("Primitiva", 1, 2, 3, 15, 16, 20)
get_ticket_loteria("Bonoloto", 1, 2, 3, 15, 16)

def get_ticket_loteria2(sorteo, *args):
  numeros_str = []
  print(f"Sorteo: {sorteo}. Los números elegidos son:")
  for num in args:
    print(num)

get_ticket_loteria2("Bonoloto", 1, 2, 3, 15, 16)

# Objetos mutables

persona1 = {
  "nombre": "Charly",
  "apellidos": "Falco",
  "edad": 39,
  "direccion": "C/ Norte 9, Madrid",
  "dni": "00000000T",
  "esta_trabajando": True
}

persona2 = persona1
persona2["nombre"] = "Steven"
print(persona2)
print(persona1)

persona3 = {
  "nombre": "Judith",
  "apellidos": persona1["apellidos"],
  "dni": persona1["dni"]
}
print(persona3)
persona3["dni"] = "00000001T"
persona1["dni"] = "00000002T"
print(persona3)
print(persona1)

lista1 = [1, 2, 3]
lista2 = lista1
lista2.append(4)
print(lista1)
print(lista2)

lista3 = []
for num in lista1:
  lista3.append(num)

lista3.append(5)
lista1.append(6)
print(lista3)
print(lista1)
print(lista2)

# * (listas), ** (dict)
lista4 = [lista3]
print(lista4)
lista4 = [*lista3]
lista4.append(10)
print(lista4)
print(lista3)

# **kwargs
persona4 = {**persona3}
persona4["nombre"] = "Juan"
print(persona4)
print(persona3)

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

# **kwargs
def filtrar_personas(lista_personas, **kwargs):
  print(kwargs)
  resultado = []
  for persona in lista_personas:
    condiciones_cumplidas = 0
    if 'filtro_trabajando' in kwargs.keys() and kwargs["filtro_trabajando"] == persona["esta_trabajando"]:
      condiciones_cumplidas = condiciones_cumplidas + 1

    if 'edad' in kwargs.keys() and kwargs["edad"] == persona["edad"]:
      condiciones_cumplidas = condiciones_cumplidas + 1

    if 'edad_mayor' in kwargs.keys() and persona["edad"] > kwargs["edad_mayor"]:
      condiciones_cumplidas = condiciones_cumplidas + 1

    if condiciones_cumplidas == len(kwargs.keys()):
      resultado.append(persona)

  return resultado

personas = [persona1, persona2, persona3]
personas_trabajando_de_30 = filtrar_personas(personas, filtro_trabajando=True, edad=30)
print(personas_trabajando_de_30)

personas_de_40 = filtrar_personas(personas, edad=40)
print(personas_de_40)
personas_de_39 = filtrar_personas(personas, edad=39)
print(personas_de_39)

personas_mayores_de_35 = filtrar_personas(personas, edad_mayor=35)
print(personas_mayores_de_35)