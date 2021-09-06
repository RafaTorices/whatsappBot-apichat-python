from mysql import MySQL


class Opciones():
    def __init__(self):
        mysql = MySQL()
        self.conexion = mysql.conexion

    def enviarOpciones(self):
        self.cursor = self.conexion.cursor()
        self.sql = 'SELECT codigo, texto FROM opciones ORDER BY codigo'
        self.cursor.execute(self.sql)
        self.resultado = self.cursor.fetchall()
        for codigo, texto in self.resultado:
            return codigo+' - '+texto
        self.conexion.close()
