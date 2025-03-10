# KayaDoc - Django + Tailwind

Este projeto é uma réplica das páginas do Kaya Doc usando Django e TailwindCSS.

## Como rodar o projeto

### 1️⃣ Modo tradicional (sem Docker)

Se você preferir rodar diretamente na sua máquina, siga esses passos:

1. Clone o repositório:
   ```sh
   git clone https://github.com/seu-usuario/kayadoc.git
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

2️⃣ Modo com Docker
Se você preferir rodar usando Docker, siga esses passos:

1. Certifique-se de ter o Docker e o Docker Compose instalados na sua máquina.

2. No diretório raiz do projeto, execute:
   ```sh
   docker-compose up --build
   ```
3. Acesse o projeto em: http://localhost:8000

4. Caso precise acessar o container, use o seguinte comando:
   ```sh
   docker-compose exec web bash
   ```