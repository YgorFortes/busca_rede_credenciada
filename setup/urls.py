from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.conf.urls.static import static
from django.conf import settings

from rest_framework.permissions import AllowAny
from src.core.log.logger import Logger, LogType

logger = Logger('GlobalExceptionHandler')

# 1. Defina as funções com nomes únicos
def error_404(request, exception):
    logger.dispatch(LogType.WARN, f'Erro 404: {request.path}')
    return JsonResponse({'mensagem': 'Página não encontrada'}, status=404)

def error_500(request):
    logger.dispatch(LogType.ERROR, f'Erro interno: {request.path}')
    return JsonResponse({'mensagem': 'Servidor com problemas! Volte mais tarde.'}, status=500)

# 2. Rotas normais
urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/v1/', include('apps.users.urls')),

]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler404 = error_404
handler500 = error_500