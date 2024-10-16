class Persona:
  # atributos de clase
  num_brazos = 2

  # Función constructora - constructor
  def __init__(self, nombre, apellidos, edad, direccion, dni):
    # Estos son atributos de instancia
    self.nombre = nombre
    self.apellidos = apellidos
    self.edad = edad
    self.direccion = direccion
    self.dni = dni

  # Métodos de instancia
  def get_nombre_completo(self):
    return f"{self.nombre} {self.apellidos}"

  def cumplir_años(self):
    self.edad = self.edad + 1
    return self.edad

  def cumplir_años2(self):
    self.edad = self.edad + 1
    print(self.edad)

  def __str__(self):
    return f"{self.nombre} {self.apellidos} {self.edad} {self.direccion} {self.dni}"

  def __repr__(self):
    return self.__str__()

  def __eq__(self, otra_persona):
    # charly == charly2
    return self.dni == otra_persona.dni

  def __ne__(self, otra_persona):
    # charly ! = charly2
    # return self.dni != otra_persona.dni
    # return not self.dni == otra_persona.dni
    return not self.__eq__(otra_persona)

  def __gt__(self, otra_persona):
    return self.edad > otra_persona.edad

  def __lt__(self, otra_persona):
    return self.edad < otra_persona.edad



charly = Persona("Charly", "Falco", 39, "C/ Norte, 29, Madrid", "00000000T")
mike = Persona("Mike", "Kozinski", 41, "C/ Norte, 51, Madrid", "00000001S")
print(f"{charly.nombre} {charly.apellidos}")
print(mike.nombre)
# mike.nombre = "Mike"
# mike.apellidos = "Kozinski"
print(charly.get_nombre_completo())
print(mike.get_nombre_completo())
print(charly.cumplir_años())
charly.cumplir_años2()
charly.cumplir_años2()
print(charly.edad)

print(mike.num_brazos)
print(charly.num_brazos)
print(Persona.num_brazos)

mike.num_brazos = 1
print(mike.num_brazos)
print(charly.num_brazos)
print(Persona.num_brazos)

lista_personas = [charly, mike]
print(charly)
print(mike.__str__())
print(lista_personas)

# charly2 = Persona("Charly", "Smith", 29, "C/ 123, Valencia", "01234567H")
charly2 = Persona("Charly", "Smith", 29, "C/ 123, Valencia", "00000000T")

if charly == charly2:
  print(f"{charly.get_nombre_completo()} es igual a {charly2.get_nombre_completo()}")
else:
  print(f"{charly.get_nombre_completo()} es diferente a {charly2.get_nombre_completo()}")

if charly < mike:
  print(f"{charly.get_nombre_completo()} es menor que {mike.get_nombre_completo()}")

if charly > mike:
  print(f"{charly.get_nombre_completo()} es mayor que {mike.get_nombre_completo()}")


class Calculadora:
  # Método estático
  def suma(n1, n2):
    return n1 + n2

  def resta(n1, n2):
    return n1 - n2

# calculadora1 = Calculadora()
print(Calculadora.suma(1, 2))
print(Calculadora.resta(8, 2))

# Herencia

class Leccion:
  def __init__(self, titulo, duracion, completada):
    self.titulo = titulo
    self.duracion = duracion
    self.completada = completada

  def completar_leccion(self):
    self.completada = True

  def __str__(self):
    # esta_completa = None
    # if self.completada:
    #   esta_completa = "x"
    # else:
    #   esta_completa = "-"
    esta_completa = "x" if self.completada else "-"
    return f"{esta_completa} {self.titulo} ({self.duracion} min)\n\n"

class LeccionTexto(Leccion):
  def __init__(self, titulo, duracion, texto, completada):
    super().__init__(titulo, duracion, completada)
    self.texto = texto

  def __str__(self):
    return f"{super().__str__()} {self.texto}"

class LeccionVideo(Leccion):
  def __init__(self, titulo, duracion, url, completada):
    super().__init__(titulo, duracion, completada)
    self.url = url

  def __str__(self):
    return f"{super().__str__()} Ver video en: {self.url}"


leccion1 = LeccionTexto("Introducción a Python", 15, "Python es un lenguaje de ...", False)
leccion2 = LeccionVideo("Comprehension list", 20, "http://curso-python.com/compehension-lists", False)

print(leccion1)
print(leccion2)
leccion1.completar_leccion()
print(leccion1)