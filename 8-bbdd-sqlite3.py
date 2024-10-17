import sqlite3

def inicializar_bbdd():
  conn = sqlite3.connect("archivos/personas.db")
  cursor = conn.cursor()

  cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
      id INTEGER PRIMARY KEY AUTOINCREMENT,  -- ID autoincremental
      nombre TEXT NOT NULL,
      email TEXT NOT NULL UNIQUE,
      password TEXT NOT NULL
  );''')

  cursor.execute('''CREATE TABLE IF NOT EXISTS informes (
      id INTEGER PRIMARY KEY AUTOINCREMENT,  -- ID autoincremental
      titulo TEXT NOT NULL,
      contenido TEXT NOT NULL,
      fecha TEXT NOT NULL,
      autor INTEGER,  -- Hace referencia a la tabla usuarios
      FOREIGN KEY (autor) REFERENCES usuarios(id)
  );''')

  conn.commit()

# inicializar_bbdd()

def añadir_usuario(nombre, email, password):
  conn = sqlite3.connect("archivos/personas.db")
  cursor = conn.cursor()

  cursor.execute('''
    INSERT INTO usuarios (nombre, email, password)
    VALUES (?, ?, ?)
  ''', (nombre, email, password))

  conn.commit()

try:
  añadir_usuario("Charly", "cfalco@gmail.com", "1234")
  añadir_usuario("Mike", "mkoz@gmail.com", "1234")
except:
  print("Alguno de los emails ya está en la BBDD")


def buscar_usuario(usuario_id):
  conn = sqlite3.connect("archivos/personas.db")
  cursor = conn.cursor()

  # cursor.execute('''
  #   select * from usuarios where id = ?
  # ''', (usuario_id,))
  cursor.execute('''
    select nombre, email from usuarios where id = ?
  ''', (usuario_id,))

  usuario = cursor.fetchone()
  print(usuario)

buscar_usuario(1)