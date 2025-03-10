# Imagem oficial do Python
FROM python:3.12.4

# Diretório de trabalho no container
WORKDIR /app

# Copia os arquivos do projeto para dentro do container
COPY . /app/

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expoe a porta do Django
EXPOSE 8000

# Comando para rodar o servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]