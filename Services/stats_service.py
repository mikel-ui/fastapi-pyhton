from repositories.users_repository import UsersRepository
from repositories.repository import users_repo,friend_requests_repo,posts_repo, likes_repo, comentarios_repo
from datetime import date, timedelta

_users = users_repo._usuarios
_friend_requests = friend_requests_repo
_posts = posts_repo
_likes = likes_repo
_comentarios = comentarios_repo

class StatsService:
    
    #post_mas_likeado_fecha(data)    
    def post_mas_likeado_fecha(self, data):
        return self.obtener_post_mas_x_fecha(data, _likes.contar_likes_de_post)

    def post_mas_comentado_fecha(self, data):
        return self.obtener_post_mas_x_fecha(data, _comentarios.contar_comentarios_de_post)
    
    def obtener_post_mas_x_fecha(self, data, contador_func):
        fecha = date(int(data.get("anio")),int(data.get("mes")),int(data.get("dia")))
        posts_fecha = _posts.obtener_posts_fecha(fecha)
        if not posts_fecha:
            return None

        post_top = posts_fecha[0]
        max_cantidad = contador_func(post_top.id)
        #como ya se tomo el valor 0, no voy a volver a pasar por el, se saltea con corchetes y ":"
        for post in posts_fecha[1:]:
            cantidad = contador_func(post.id)
            if cantidad > max_cantidad:
                post_top = post
                max_cantidad = cantidad

        return post_top
                            
    def obtener_posts_mas_x_comentarios(self, data):
        return self.obtener_posts_con_mas_x(data, _comentarios.contar_comentarios_de_post, "cant_comentarios")

    def obtener_posts_mas_x_likes(self, data):
        return self.obtener_posts_con_mas_x(data, _likes.contar_likes_de_post, "cant_likes")

    def obtener_posts_con_mas_x(self, data, contador_func, clave_cantidad):
        posts_filtrados = []
        cantidad_minima = int(data.get(clave_cantidad, 0))
        
        for post in posts_repo._posts.values():
            cantidad_actual = contador_func(post.id)
            if cantidad_actual > cantidad_minima:
                posts_filtrados.append(post)
        
        return posts_filtrados

    #############################################################################################################
    #Quiénes son los usuarios más activos del día: los usuarios más activos de un día en particular son aquellos que han superado el 60% de la cantidad total de posts permitidos diarios.
    def obtener_activos(self):
        usuarios_activos = []
        fecha = date.today.strftime('%Y-%m-%d')
        for usuario in _users.values():
            cantidad_posts_fecha = _posts.contar_posts_fecha(usuario.id,fecha)
            if cantidad_posts_fecha>3:
                usuarios_activos.append(usuario)
        return usuarios_activos
    
    #Quiénes son los usuarios que postean poco. Un usuario postea “poco” cuando ha realizado como máximo 1 post por semana en las últimas 4 semanas
    def obtener_pasivos(self):
        fecha_hoy = date.today.strftime('%Y-%m-%d')
        fecha_limite = fecha_hoy - timedelta(weeks=4) #hace cuatro semanas
        usuarios_pasivos = []
        
        for usuario in _users.values():
            cantidad_posts_rango_fechas = _posts.contar_posts_rango_fecha(usuario.id,fecha_limite,fecha_hoy)
            if cantidad_posts_rango_fechas<=1:
                usuarios_pasivos.append(usuario)
        return usuarios_pasivos                    
    
    #Escritores = "escriben mucho". Un usuario escribe mucho cuando al menos en el 70% de sus posts alcanzó el 90% de caracteres máximos permitidos.
    def obtener_escritores(self):
        escritores = []        
        for usuario in _users.values():            
            setenta_porciento = _posts.listar_posts_de_un_usuario(usuario.id)*0.7
            cantidad_posts_superan_caracteres = len(_posts.posts_superan_caracteres(usuario.id,3000*0.9))
            if cantidad_posts_superan_caracteres>setenta_porciento:
                escritores.append(usuario)
        return escritores
    
    ############################################################################################################
    def top_n_usuarios_mas_spammers(self, data):
        usuarios_spammers = []
        spammer_delimitador = int(data.get("delimitador"))

        cantidad_top_spammers = int(data.get("top-n"))
        cant_aux = 0
        
        for usuario in _users.values():
            cant_aux = len(_friend_requests.listar_solicitudes_enviadas_pendientes(usuario.id))
            if cant_aux>spammer_delimitador:
                if len(usuarios_spammers)<cantidad_top_spammers:
                    usuarios_spammers.append(usuario)
        
        #Un usuario es "spammer" cuando tiene más de X solicitudes de amistad enviadas pendientes de aceptación.
        return usuarios_spammers

    def top_n_usuarios_mas_callados(self,data):
        usuarios_callados = []
        callado_delimitador = int(data.get("delimitados"))
        
        cantidad_top_callados= int(data.get("top-n"))
        cant_aux = 0
        
        for usuario in _users.values():
            cant_aux = usuario.cantidad_amigos()
            if cant_aux<callado_delimitador:
                if len(usuarios_callados)<cantidad_top_callados:
                    usuarios_callados.append(usuario)        
        return usuarios_callados
    
    def top_n_usuarios_rechazados(self,data):
        usuarios_rechazados = []        
        cantidad_top_rechazados = int(data.get("top-n"))
                
        cant_aux = 0        
        for usuario in _users.values():
            cant_aux = len(_friend_requests.listar_falsos_amigos(usuario.id))
            if cant_aux>=1:
                if len(usuarios_rechazados)<cantidad_top_rechazados:
                    usuarios_rechazados.append(usuario)

        return usuarios_rechazados

    def obtener_cantidad_usuarios_por_gustos(self, data):
        resultado = []
        gustos_musicales = data.get("gustos-musicales", [])
        if isinstance(gustos_musicales, list):
            for gusto in gustos_musicales:
                cantidad_usuarios_por_gusto = self.obtener_cantidad_usuarios_por_gusto(gusto)
                resultado.append({
                    "gusto_musical":gusto,
                    "cantidad usuarios":cantidad_usuarios_por_gusto
                })
        else:
            cantidad_usuarios_por_gusto = self.obtener_cantidad_usuarios_por_gusto(gusto_musical=gustos_musicales)
            resultado.append({
                "gusto_musical":gustos_musicales,
                "cantidad usuarios":cantidad_usuarios_por_gusto
            })        
        return resultado
        
    def obtener_cantidad_usuarios_por_gusto(self, gusto_musical):
        #opc 1:
        #print(_users_repo._usuarios.get(1).gustos_musicales) #Leo Fernandez (leolibros@gmail.com)
        #print(_users_repo._usuarios.get(2).gustos_musicales) #Luca Viliani (luca@gmail.com)
        #opc 2:
        # for userId in _users_repo._usuarios:
        #     print(_users_repo._usuarios.get(userId))
        #opc 3:
        # for user in _users.values():
        #     print(user.gustos_musicales)
        return len(list(filter((lambda user: (gusto_musical in user.gustos_musicales)),_users.values())))