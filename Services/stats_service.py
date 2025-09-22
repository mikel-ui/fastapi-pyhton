from repositories.users_repository import UsersRepository
from repositories.repository import users_repo

_users = users_repo._usuarios

class StatsService:
        
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