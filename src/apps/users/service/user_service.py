from core.log.logger import Logger, LogType
from ..repository.user_repository import UserRepository
from core.erros.custom_http_error import CustomHttpError
from ..models.user_model import  Usuario, CreateUsuarioDTO

from datetime import datetime
from typing import Optional

from rest_framework import status


logger = Logger('UserService')

class UserService():
    def __init__(self, repository: UserRepository):
        self.repository = repository or UserRepository()

    def create_user(self, userDto:CreateUsuarioDTO):
      
        
        if not userDto.nome_usuario or not userDto.login or not userDto.senha or not userDto.cargo:
            raise CustomHttpError('Campos obrigatórios ausentes.', status.HTTP_400_BAD_REQUEST)
        
        
        
        user_exist = self.find_user_by_login(userDto.login)
     
        
        if user_exist:
            raise CustomHttpError('Usuário já cadastrado.', status.HTTP_409_CONFLICT,)
        

        new_user_dto = CreateUsuarioDTO(
            nome_usuario=userDto.nome_usuario,
            login=userDto.login,
            senha=userDto.senha,
            cargo=userDto.cargo
        )
        
        return self.repository.create(new_user_dto)
    
    
    def find_user_by_login(self, login: str) -> Optional[Usuario]:
        if not login:
            raise CustomHttpError('Campos obrigatórios ausentes.', status.HTTP_400_BAD_REQUEST)
        
        user = self.repository.find_user_by_login(login)

        
        return user
    

    
               

            
    