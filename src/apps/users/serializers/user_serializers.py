from rest_framework import serializers 


class CreateUserSerializer(serializers.Serializer):
    nome_usuario = serializers.CharField(max_length=45)
    login = serializers.CharField(max_length=45)
    senha = serializers.CharField(write_only= True)
    cargo = serializers.CharField(max_length=45)
    
    

class UserProfileResponseSerializer(serializers.Serializer):
   pass
    
class AutenticateUser(serializers.Serializer):
    pass

