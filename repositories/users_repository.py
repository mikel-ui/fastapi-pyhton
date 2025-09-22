from entities.user import Usuario

class UsersRepository:
    def __init__(self):
        self._usuarios = {}  # Un solo diccionario que almacena usuarios por ID
        self._next_id = 1

    def next_id(self):
        current_id = self._next_id
        self._next_id += 1
        return current_id

    def crar_amistad(self,id_emisor,id_receptor):
        self._usuarios.get(id_emisor).agregar_amigo(id_receptor)
        self._usuarios.get(id_receptor).agregar_amigo(id_emisor)
        return str(self._usuarios.get(id_emisor).nombre)+" y "+str(self._usuarios.get(id_receptor).nombre)+" ahora son amigos!"
         
    

    def listar_usuarios(self):
        return list(self._usuarios.values())

    def obtener(self, id_):
        return self._usuarios.get(id_)

    def obtener_lista_de_ids(self):
        return [usuario.id for usuario in self._usuarios.values()]

    def obtener_por_email(self, email):
        # Buscar en todos los usuarios por email
        for usuario in self._usuarios.values():
            if usuario.email == email:
                return usuario                
        return None

    def actualizar(self, usuario):
        # Actualizar el usuario en el diccionario
        self._usuarios[usuario.id] = usuario
        return usuario

    def guardar(self, usuario):
        # Guardar el usuario en el diccionario
        self._usuarios[usuario.id] = usuario
        return usuario