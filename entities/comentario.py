

class Comentario:
    def __init__(self, id: int, id_emisor : int, id_post_destinatario:int, cuerpo:str):
        self.id = id
        self.id_emisor = id_emisor
        self.id_post_destinatario = id_post_destinatario
        self.cuerpo = cuerpo