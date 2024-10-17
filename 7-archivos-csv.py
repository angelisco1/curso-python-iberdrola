import csv

with open("archivos/trabajadores.csv", "w", newline="") as file:
  writer = csv.writer(file)
  writer.writerow(["nombre", "apellido", "dni"])
  writer.writerow(["Charly", "Falco", "0000000T"])
  writer.writerow(["Mike", "Kozinski", "0000001S"])

class Trabajador:
  def __init__(self, nombre, apellidos, dni):
    self.nombre = nombre
    self.apellidos = apellidos
    self.dni = dni

  def get_email(self):
    return f"{self.nombre[0]}{self.apellidos}@gmail.com"

lista_trabajadores = []
with open("archivos/trabajadores.csv", "r") as file:
  reader = csv.reader(file)
  for posicion, linea in enumerate(reader):
    print(linea)
    if posicion != 0:
      lista_trabajadores.append(Trabajador(linea[0], linea[1], linea[2]))

for trabajador in lista_trabajadores:
  print(trabajador.get_email())