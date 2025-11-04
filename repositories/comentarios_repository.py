from entities.comentario import Comentario

class ComentariosRepository:
    def __init__(self):
        self._comentarios = {}
        self._next_id = 1

    def next_id(self):
        current_id = self._next_id
        self._next_id += 1
        return current_id
    
    def guardar(self, comentario):
        # Guardar el comentario en el diccionario
        self._comentarios[comentario.id] = comentario
        return comentario
    
    def listar_comentarios_de_post(self, id_post):
        comentarios = []
        for comentario in self._comentarios.values():
            if comentario.id_post_destinatario == id_post:
                comentarios.append(comentario)
        return comentarios
    
    def contar_comentarios_de_post(self, id_post):
        return len(self.listar_comentarios_de_post(id_post))
        
        