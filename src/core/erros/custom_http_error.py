class CustomHttpError(Exception):
    def __init__(self, message='Problemas no servidor! Volte mais tarde', status_code=500):
        self.message = message
        self.status_code = status_code
        super().__init__(message)
        


