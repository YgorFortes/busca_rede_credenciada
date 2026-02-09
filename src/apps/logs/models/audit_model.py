from django.db import models
from django.conf import settings
import json
from django.core.exceptions import ValidationError

class AuditLog(models.Model):
    username = models.CharField(max_length=255, null=True, blank=True) 
    
    method = models.CharField(max_length=10)
    path = models.CharField(max_length=255)
    body = models.JSONField(null=True, blank=True)
    
    level = models.CharField(max_length=20)
    
    message = models.TextField()
    
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.CharField(max_length=255, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    @classmethod
    def log(cls, username, method, path, body=None, level='INFO', message='', ip_address=None, user_agent=None):
        # Altere para salvar o username diretamente, não mais o user.
        log_entry = cls(
            username=username,
            method=method,
            path=path,
            body=body,
            level=level,
            message=message,
            ip_address=ip_address,
            user_agent=user_agent
        )
        log_entry.save()

    def __str__(self):
        return f"{self.level} | {self.username} | {self.path} | {self.created_at}"

