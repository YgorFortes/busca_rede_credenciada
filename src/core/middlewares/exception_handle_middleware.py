from django.http import JsonResponse
from django.http import Http404
from rest_framework.exceptions import ValidationError as DRFValidationError
from rest_framework import serializers
from django.conf import settings


from core.erros.custom_http_error import CustomHttpError
from core.log.logger import Logger, LogType



logger = Logger('GlobalExceptionHandler')


class GlobalExceptionMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    # 🔹 Executa ANTES da view
    def process_request(self, request, exception):
        logger.dispatch(
        LogType.ERROR,
            f"Exceção no middleware para {request.path}: {str(exception)}"
        )
        return None

    # 🔹 Executa SOMENTE quando ocorre exceção
    def process_exception(self, request, exception):
        if request.path.startswith(settings.STATIC_URL):
            return None 

        logger.dispatch(LogType.ERROR, f"Tipo de exceção: {type(exception)}")
        logger.dispatch(LogType.DEBUG, f"Detalhes da exceção: {type(exception)}")

        # ===== DRF ValidationError =====
        if isinstance(exception, DRFValidationError):
            errors = exception.detail

            logger.dispatch(
                LogType.WARN,
                f'Erro de validação DRF: {errors}, Endpoint: {request.path}'
            )

            return JsonResponse({
                'mensagem': 'Erro de validação nos dados enviados.',
                'erros': errors
            }, status=400)

        # ===== Serializer ValidationError =====
        if isinstance(exception, serializers.ValidationError):
            errors = exception.detail

            logger.dispatch(
                LogType.WARN,
                f'Erro de validação Serializer: {errors}, Endpoint: {request.path}'
            )

            return JsonResponse({
                'mensagem': 'Erro de validação nos dados enviados.',
                'erros': errors
            }, status=400)

        # ===== Erro HTTP personalizado =====
        if isinstance(exception, CustomHttpError):
            logger.dispatch(
                LogType.ERROR,
                f'Erro personalizado: {exception.message}, Endpoint: {request.path}'
            )

            return JsonResponse(
                {'mensagem': exception.message},
                status=exception.status_code
            )

        # ===== 404 =====
        if isinstance(exception, Http404):
            user = request.user 

            logger.dispatch(
                LogType.WARN,
                f'Erro 404: {request.path}, User: {user}'
            )

            return JsonResponse(
                {'mensagem': 'Página não encontrada'},
                status=404
            )
            
            return None

        # ===== Erro genérico =====
        logger.dispatch(
            LogType.ERROR,
            f'Erro interno: {str(exception)}, Endpoint: {request.path}'
        )

        return JsonResponse(
            {'mensagem': 'Servidor com problemas! Volte mais tarde.'},
            status=500
        )

    def __call__(self, request):
        response = self.get_response(request)
        return response
