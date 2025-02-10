# Usa a imagem oficial do Python
FROM python:3.12

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos do projeto para dentro do container
COPY . .

# Instala as dependências do projeto
RUN pip install --no-cache-dir django gunicorn psycopg2-binary

# Expõe a porta usada pelo Django
EXPOSE 8000

# Comando para rodar o servidor do Django
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "python_django_project.wsgi:application"]

