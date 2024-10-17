import psycopg2

def inicializar_bbdd():
  conn = psycopg2.connect(
    dbname="usuarios",
    user="postgres",
    password="postgres",
    port="5432",
    host="localhost"
  )
  cursor = conn.cursor()

  cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
      id SERIAL PRIMARY KEY,
      nombre VARCHAR(100) NOT NULL,
      email VARCHAR(100) NOT NULL UNIQUE,
      password VARCHAR(100) NOT NULL
  );''')

  cursor.execute('''CREATE TABLE IF NOT EXISTS informes (
    id SERIAL PRIMARY KEY,
    titulo TEXT NOT NULL,
    contenido TEXT NOT NULL,
    fecha TIMESTAMP NOT NULL,
    autor INTEGER REFERENCES usuarios(id) ON DELETE CASCADE
  );''')

  conn.commit()
  conn.close()

# inicializar_bbdd()

def añadir_usuario(nombre, email, password):
  conn = psycopg2.connect(
    dbname="usuarios",
    user="postgres",
    password="postgres",
    port="5432",
    host="localhost"
  )
  cursor = conn.cursor()

  cursor.execute('''
    INSERT INTO usuarios (nombre, email, password)
    VALUES (%s, %s, %s);
  ''', (nombre, email, password))

  conn.commit()

try:
  añadir_usuario("Charly", "cfalco@gmail.com", "1234")
  añadir_usuario("Mike", "mkoz@gmail.com", "1234")
except:
  print("Alguno de los emails ya está en la BBDD")


def buscar_usuario(usuario_id):
  conn = psycopg2.connect(
    dbname="usuarios",
    user="postgres",
    password="postgres",
    port="5432",
    host="localhost"
  )
  cursor = conn.cursor()

  # cursor.execute('''
  #   select * from usuarios where id = %s
  # ''', (usuario_id,))
  cursor.execute('''SELECT nombre, email FROM usuarios WHERE id = %s''', (usuario_id,))

  usuario = cursor.fetchone()
  print(usuario)

buscar_usuario(1)