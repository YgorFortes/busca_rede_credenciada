FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instala dependências de sistema (incluindo nodejs, npm e locale)
RUN apt-get update && apt-get install -y \
    build-essential libpq-dev postgresql-client curl locales \
    libpango-1.0-0 libpangoft2-1.0-0 \
    libcairo2 libgdk-pixbuf-xlib-2.0-0 \
    libffi-dev shared-mime-info \
    && curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs \
    && echo "pt_BR.UTF-8 UTF-8" > /etc/locale.gen \
    && locale-gen pt_BR.UTF-8 \
    && rm -rf /var/lib/apt/lists/*

# Define variáveis de ambiente para o locale
ENV LANG=pt_BR.UTF-8
ENV LANGUAGE=pt_BR:pt
ENV LC_ALL=pt_BR.UTF-8
ENV PYTHONPATH=/app:/app/src




COPY requirements.txt ./

# Instala pacotes Python
RUN pip install --upgrade pip && pip install -r requirements.txt



# Copia todo código da aplicação
COPY . .



# Coleta arquivos estáticos do Django
RUN python manage.py collectstatic --noinput

EXPOSE 8000




