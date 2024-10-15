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
def get_ticket_loteria(sorteo, *args):
  numeros_str = []
  for num in args:
    numeros_str.append(str(num))
  print(f"Sorteo: {sorteo}. Los números elegidos son: {' - '.join(numeros_str)}")

get_ticket_loteria("Primitiva", 1, 2, 3, 15, 16, 20)