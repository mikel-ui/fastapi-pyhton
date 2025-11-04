from entities.like import Like

class LikesRepository:
    ##############################################################################################################################
    def __init__(self):
        self._likes = {}
        self._next_id = 1
        
    def next_id(self):
        current_id = self._next_id
        self._next_id += 1
        return current_id
    
    def guardar(self, like):
        # Guardar el like en el diccionario
        self._likes[like.id] = like
        return like
    
    def contar_likes_emisor_destinatario(self, id_post_destinatario, id_usuario_emisor):
        return len()        
    
    def obtener_likes_emisor_destinatario(self, id_post_destinatario, id_usuario_emisor):
        likes = []
        for like in self._likes.values():
            if like.id_emisor == id_usuario_emisor and like.id_post_destinatario == id_post_destinatario:
                likes.append(like)
        return likes
    ##############################################################################################################################
    
    def listar_likes_de_post(self, id_post):
        likes = []
        for like in self._likes.values():
            if like.id_post_destinatario == id_post:
                likes.append(like)
        return likes
    
    def contar_likes_de_post(self, id_post):
        return len(self.listar_likes_de_post(id_post))