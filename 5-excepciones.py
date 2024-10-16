from getpass import getpass

# Input de datos
nombre = input("Introduce tu nombre: ")
password = getpass("Introduce tu contraseña: ")
print(f"Bienvenido {nombre} ({password})")