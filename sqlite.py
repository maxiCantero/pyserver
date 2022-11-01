import sqlite3
con = sqlite3.connect('test')
cursor = con.cursor()
print ("la base de datos se abrió correctamente")

cursor.execute('''CREATE TABLE IF NOT EXISTS empresa
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            edad INT NOT NULL,
            direccion CHAR(50),
            salario REAL)''')
print("Tabla creada correctamente")

cursor.execute("INSERT INTO empresa (nombre,edad,direccion,salario) VALUES('Pablo',32,'Maldonado',15000.00)")

con.commit()
print("se guardo correctamente")