from core.log.logger import Logger, LogType
from ..repository.user_repository import UserRepository
from core.erros.custom_http_error import CustomHttpError


from rest_framework import status


logger = Logger('UserService')

class UserService():
    def __init__(self, repository: UserRepository):
        self.repository = repository or UserRepository()

    def find_user_by_id(self, user_id: str): 
        if not user_id:
            raise CustomHttpError('O ID do usuário é obrigatório.')
            
        user = self.repository.find_user_by_id(user_id=user_id)
            
        if not user:
            raise CustomHttpError('Usuário não encontrado.', status.HTTP_404_NOT_FOUND)
            
        return user
        

 
    
    

    
               

            
    