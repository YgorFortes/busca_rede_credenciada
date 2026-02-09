from datetime import date, datetime
class UserEntity:
    def __init__(self, id: int, nome:str, username:str, matricula:str, setor:str= None, diretoria:str =None,  created_at=date, updated_at=date, deleted_at=date):
        self.id = id
        self.nome = nome
        self.username = username
        self.matricula = matricula
        self.setor = setor
        self.diretoria = diretoria
        self.created_at = datetime.now()
        self.deleted_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "username": self.username
        }
        
