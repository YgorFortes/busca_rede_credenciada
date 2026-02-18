from rest_framework.views import APIView
from djangorestframework_camel_case.render import CamelCaseJSONRenderer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError as DRFValidationError

from ..service.user_service import UserService
from ..repository.user_repository import UserRepository
from ..serializers.user_serializers import  CreateUserSerializer
from ..models.user_model import  Usuario, CreateUsuarioDTO

user_service = UserService(repository=UserRepository())  


class CreateUserView(APIView):
    renderer_classes = [CamelCaseJSONRenderer]
    
    def post(self, request):
        serializer_user = CreateUserSerializer(data=request.data)
        
        if not serializer_user.is_valid():
            return Response(serializer_user.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
        user_dto = CreateUsuarioDTO(
            **serializer_user.validated_data
        )
        
        
        usuario = user_service.create_user(user_dto)
        
        return Response(
            {
                "id": usuario.id,
                "nomeUsuario": usuario.nome_usuario,
                "login": usuario.login,
                "cargo": usuario.cargo,
            }, status=status.HTTP_201_CREATED
        )
    
        
        
        

