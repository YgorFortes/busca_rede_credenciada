from ..models.user_model import  Usuario, CreateUsuarioDTO, UsuarioPublic
from django.db import connection
from typing import Optional

class UserRepository:
    def __init__(self):
        self.model =Usuario
    
    def create(self, userDto: CreateUsuarioDTO) -> Usuario:
        

        query = '''
            INSERT INTO usuario
            (nome_usuario, login, senha, cargo)
            VALUES (%s, %s, %s, %s)
            RETURNING id, nome_usuario, login, senha, cargo,
            created_at, updated_at, deleted_at  
        '''
            
        params = (
            userDto.nome_usuario,
            userDto.login,
            userDto.senha,
            userDto.cargo
        )
            
        
        with connection.cursor() as cursor:

            cursor.execute(query, params)
            
            row = cursor.fetchone()
            
            return Usuario(*row)
    
    
    def find_user_by_login(self, login)->Optional[UsuarioPublic]:  
        
        query = '''
            SELECT nome_usuario, login, cargo  from usuario
            WHERE login = %s and deleted_at  IS NULL
        '''
        
        params = (
            login,
        )
        
        
        with connection.cursor() as cursor:
            cursor.execute(query, params)
            
            row = cursor.fetchone()
            
            if not row:
                return None
            
            return UsuarioPublic(*row)
    


    

