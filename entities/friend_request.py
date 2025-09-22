from typing import List
from datetime import date

class FriendRequest:
    def __init__(self, id: int, id_emisor: int, id_receptor: int, estado: str):
        self.id = id
        self.id_emisor = id_emisor
        self.id_receptor = id_receptor
        self.estado = estado
        self.fecha = date.today().strftime('%Y-%m-%d')
        
    def aceptar(self):
        self.estado = "aceptada"