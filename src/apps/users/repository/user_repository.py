from ..models.user_model import  Usuario



from typing import Optional

class UserRepository:
    def __init__(self):
        self.model =Usuario
    
    def find_user_by_id(self, user_id:str)->Optional[Usuario]:
        user = self.model.objects.filter(id=user_id).first()
        return user


    

