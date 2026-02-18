from django.urls import path
from .views.user_view import CreateUserView

urlpatterns = [
    path("create_user", CreateUserView.as_view(), name="create_user"),
]