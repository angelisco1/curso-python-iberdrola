# Comprehension lists

numeros = [1, 2, 3]
doble_numeros = [num * 2 for num in numeros]
print(doble_numeros)


persona1 = {
  "nombre": "charly",
  "apellidos": "falco",
  "edad": 39,
  "direccion": "C/ Norte 9, Madrid",
  "dni": "00000000T",
  "esta_trabajando": True
}

persona2 = {
  "nombre": "mike",
  "apellidos": "kozinski",
  "edad": 41,
  "direccion": "C/ Norte 12, Madrid",
  "dni": "00000001S",
  "esta_trabajando": False
}

persona3 = {
  "nombre": "octavia",
  "apellidos": "blake",
  "edad": 30,
  "direccion": "C/ Este 2, Madrid",
  "dni": "00000003E",
  "esta_trabajando": True
}

lista_personas = [persona1, persona2, persona3]

nombres_personas = [persona["nombre"].title() for persona in lista_personas]
print(nombres_personas)

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


personas_que_trabajan = filtrar_personas(lista_personas, filtro_trabajando=True)
nombres_completos_trabajadores = [f"{persona['nombre']} {persona['apellidos']}" for persona in personas_que_trabajan]
print(nombres_completos_trabajadores)

emails_personas = [f"{persona['nombre'][0]}{persona['apellidos']}@gmail.com" for persona in lista_personas if persona["esta_trabajando"]]
print(emails_personas)

lista_productos = ["Tomates", "Patatas", "Cebollas"]
lista_ventas = [100, 200, 120]


# datos = []
# for posicion, producto in enumerate(lista_productos):
#   datos.append((producto, lista_ventas[posicion]))
datos = [(producto, lista_ventas[posicion]) for posicion, producto in enumerate(lista_productos)]
print(datos)


# lista_tuplas = []
# for pos_producto, producto in enumerate(lista_productos):
#   for pos_venta, venta in enumerate(lista_ventas):
#     if pos_producto == pos_venta:
#       lista_tuplas.append((producto, venta))
datos = [(producto, venta) for pos_producto, producto in enumerate(lista_productos) for pos_venta, venta in enumerate(lista_ventas) if pos_producto == pos_venta]
print(datos)

# Dict comprehensions
sugus = {
  "piña": "azul",
  "fresa": "rojo",
  "limón": "amarillo",
  "naranja": "naranja",
  "frambuesa": "morado",
  "manzana": "verde"
}

sugus_invertidos = {color: sabor for sabor, color in sugus.items()}
print(sugus_invertidos)
# [(piña, azul), (limón, amarillo), (...)]

texto = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Totam quod nam sequi aut temporibus maxime? Placeat asperiores voluptate sunt quod laboriosam enim cumque iure aliquam ipsum laudantium nihil, ex molestias."
# {
#   Lorem: 5,
#   ipsum: 5,
#   dolor: 5,
#   sit: 3,
# }
print("Winter is coming".split(" "))

longitud_palabras = {palabra: len(palabra) for palabra in texto.replace(".", "").replace(",", "").replace("?", "").split(" ")}
print(longitud_palabras)