from rest_framework.views import APIView
from djangorestframework_camel_case.render import CamelCaseJSONRenderer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError as DRFValidationError


from ..service.user_service import UserService
from ..repository.user_repository import UserRepository
from ..serializers.user_serializers import UserProfileResponseSerializer


user_service = UserService(repository=UserRepository())  


class ProfileView(APIView):
    renderer_classes = [CamelCaseJSONRenderer]
    
    def get(self, request):
        pass

