from typing import List
from datetime import date

class Post:
    def __init__(self, id: int, id_creador : int, titulo: str, cuerpo: str):
        self.id = id
        self.id_creador = id_creador
        self.titulo = titulo
        self.cuerpo = cuerpo
        self.fecha_creacion = date.today().strftime('%Y-%m-%d')
            
    def contar_caracteres_cuerpo(self):
        return len(self.cuerpo)