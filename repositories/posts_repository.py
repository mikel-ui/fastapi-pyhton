from entities.post import Post

class PostsRepository:
    def __init__(self):
        self._posts = {}
        self._next_id = 1

    def obtener_post(self, id_post):
        for post in self._posts.values():
            if post.id==id_post:
                return post

    #cantidad_posts_rango_fechas = _posts.contar_posts_rango_fecha(usuario.id,fecha_limite,fecha_hoy)
    def contar_posts_rango_fecha(self,usuario_id,fecha_desde,fecha_hasta):
        return len(self.obtener_posts_rango_fecha(usuario_id,fecha_desde,fecha_hasta))
    
    def obtener_posts_rango_fecha(self,usuario_id,fecha_desde,fecha_hasta):
        posts_rango_fecha = []
        posts_usuario = self.obtener_posts_de_usuario(usuario_id)
        for post in posts_usuario:
            if post.fecha_creacion >= fecha_desde and post.fecha_creacion <= fecha_hasta:
                posts_rango_fecha.append(post)
        return posts_rango_fecha                    
    
    def obtener_posts_fecha(self, fecha):
        posts_fecha = []
        for post in self._posts.values():
            if post.fecha_creacion == fecha:
                posts_fecha.append(post)
        return posts_fecha
        
    def obtener_posts_de_usuario(self, usuario_id):
        posts = []
        for post in self._posts.values():
            if post.id_creador==usuario_id:
                posts.append(post)
        return posts

    def contar_posts_de_un_usuario(self,id_creador):
        return len(self.listar_posts_de_un_usuario(id_creador))

    def posts_superan_caracteres(self, usuario_id,cantidad_caracteres):
        posts_superan = []
        posts_usuario = self.listar_posts_de_un_usuario(usuario_id)
        for post in posts_usuario:
            if post.contar_caracteres_cuerpo()>cantidad_caracteres:
                posts_superan.append(post)
        return posts_superan
        

    def listar_posts_de_un_usuario(self,id_creador):
        posts_usuario = []
        for post in self._posts.values():
            if post.id_creador == id_creador:
                posts_usuario.append(post)
        return posts_usuario

    def se_puede_agregar(self,usuario_id,fecha_creacion):
        # para agregar post se necesita:
        #   -no haber 5 el mismo dia
        #   -no tener mas de 3000 caracteres
        return not(self.contar_posts_fecha(usuario_id,fecha_creacion)>=5)            
    
    def contar_posts_fecha(self,id,fecha):
        cant_post = 0
        for post in self._posts.values():
            if post.id_creador == id:
                if post.fecha_creacion==fecha:
                    cant_post += 1
        return cant_post
                        
    def agregar(self,friend_request):
        self._friend_requests[friend_request.id] = friend_request
        return friend_request
    
    def next_id(self):
        current_id = self._next_id
        self._next_id += 1
        return current_id
    
    def guardar(self, post):
        # Guardar el post en el diccionario
        self._posts[post.id] = post
        return post