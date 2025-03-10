# Clone KayaDoc - Django + Tailwind

Este projeto é uma réplica das páginas do Kaya Doc usando Django e TailwindCSS.

![12](https://github.com/user-attachments/assets/46b3420b-2064-4b50-bc08-3221d42ef4e1)

## Como rodar o projeto

### 1️⃣ Modo tradicional (sem Docker)

Se você preferir rodar diretamente na sua máquina, siga esses passos:

1. Clone o repositório:
   ```sh
   git clone https://github.com/LucaswmLima//kayadoc.git
   cd kayadoc
   ```

2. Crie e ative um ambiente virtual:
   ```sh
   python -m venv venv
   source venv/bin/activate  # No Windows, use: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

4. Execute as migrações do banco de dados:
   ```sh
   python manage.py migrate
   ```

5. Execute o servidor Django:
   ```sh
   python manage.py runserver
   ```

6. Acesse o projeto em: http://127.0.0.1:8000 (Porta padrão)

### 2️⃣ Modo com Docker
Se você preferir rodar usando Docker, siga esses passos:

1. Clone o repositório:
   ```sh
   git clone https://github.com/LucaswmLima//kayadoc.git
   cd kayadoc
   ```

2. Certifique-se de ter o Docker e o Docker Compose instalados na sua máquina.

3. No diretório raiz do projeto, execute:
   ```sh
   docker-compose up --build
   ```
4. Acesse o projeto em: http://localhost:8000

5. Caso precise acessar o container, use o seguinte comando:
   ```sh
   docker-compose exec web bash
   ```
