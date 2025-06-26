﻿<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">

<h3 align="center">KayaDoc Clone</h3>

  <p align="center">
    Projeto da página madicos do site KayaDoc usando Django e TailwindCSS.
    <br />
    <a href="https://github.com/lucaswmlima/kayadoc"><strong>Explore a documentação »</strong></a>
    <br />
    <br />
    ·
    <a href="https://github.com/lucaswmlima/kayadoc/issues">Reportar Bug</a>
    ·
    <a href="https://github.com/lucaswmlima/kayadoc/issues">Solicitar Recurso</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Índice</summary>
  <ol>
    <li>
      <a href="#sobre-o-projeto">Sobre o Projeto</a>
      <ul>
        <li><a href="#tecnologias-utilizadas">Tecnologias Utilizadas</a></li>
      </ul>
      <ul>
        <li><a href="#funcionalidades">Funcionalidades</a></li>
      </ul>
    </li>
    <li>
      <a href="#utilização">Utilização</a>
      <ul>
        <li><a href="#Como rodar o projeto">Como rodar o projeto</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contribuindo">Contribuindo</a></li>
    <li><a href="#licença">Licença</a></li>
    <li><a href="#contato">Contato</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## Sobre o projeto

Desenvolvido com Python, Django, Tailwind CSS, SQLite e Docker, este projeto replica a funcionalidade da plataforma real da KayaDoc com foco na listagem de médicos. A aplicação inclui filtros dinâmicos, pesquisa por tags, preço e avaliações, além de uma interface personalizada para cada médico.
O sistema foi construído com ênfase em organização do código e boas práticas de desenvolvimento, atendendo aos requisitos funcionais e adicionais da plataforma original.
Este repositório é uma versão sanitizada (clone) do projeto real, com dados fictícios utilizados exclusivamente para fins de demonstração técnica e debug, garantindo a proteção de informações sensíveis.

![](https://github.com/user-attachments/assets/f1ec9437-6a98-462c-9444-f3381461eeb1)

<p align="right">(<a href="#readme-top">de volta ao topo</a>)</p>

## Link do Projeto Hospedado
https://kayadoc.onrender.com


## Tecnologias Utilizadas
* [![Python][Python]][Python-url]
* [![Django][Django]][Django-url]
* [![Sqlite][Sqlite]][Sqlite-url]
* [![Docker][Docker]][Docker-url]
* [![Tailwindcss][Tailwindcss]][Tailwindcss-url]

<p align="right">(<a href="#readme-top">de volta ao topo</a>)</p>

## Funcionalidades

### Filtros Dinâmicos
* Permite que os usuários filtrem a lista de médicos por especialidade, preço e avaliações, proporcionando uma busca personalizada.

### Pesquisa Avançada
* Os usuários podem pesquisar médicos por tags, faixa de preço e visualizações, ajudando a encontrar resultados mais específicos.

### Lista de Médicos Atualizada
* A lista de médicos é alimentada por um banco de dados SQLite, garantindo que os dados estejam sempre atualizados.

### Página de Médico Personalizada
* Cada página de médico exibe informações dinâmicas, como foto de perfil, foto de fundo, descrições e avaliações (estrelas e visualizações), todas atualizáveis em tempo real.

<!-- GETTING STARTED -->
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

6. Acesse o projeto em: http://127.0.0.1:8000/  (Porta padrão)


### 2️⃣ Modo com Docker
Se você preferir rodar usando Docker, siga esses passos:

1. Clone o repositório:
   ```sh
   git clone https://github.com/LucaswmLima//kayadoc.git
   cd kayadoc
   ```

2. Certifique-se de ter o Docker instalado na sua máquina.

3. Certifique-se de que a Docker Engine está funcionando, caso haja execute o seguinte comando

   ```sh
   docker info
   ```

4. No diretório raiz do projeto, execute:
   ```sh
   docker-compose up --build
   ```
5. Acesse o projeto em: http://localhost:8000/  (Porta padrão)

6. Caso precise acessar o container, use o seguinte comando:
   ```sh
   docker-compose exec web bash
   ```

<p align="right">(<a href="#readme-top">de volta ao topo</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Criar o projeto Django
- [x] Configurar o ambiente virtual
- [x] Instalar o TailwindCSS
- [x] Configurar o Docker para o projeto
- [x] Criar o modelo de dados para médicos no Django
- [x] Criar o modelo de dados para formacoes dos medicos no Django
- [x] Configurar o banco de dados SQLite
- [x] Realizar a migração do banco de dados
- [x] Criar a página de base
- [x] Criar a página de listagem de médicos
- [x] Criar a página de perfil de médico
- [x] Estilizar as páginas com TailwindCSS
- [x] Testar as páginas localmente
- [x] Testar as páginas no Docker

      
Veja [open issues](https://github.com/lucaswmlima/kayadoc/issues) para uma lista completa de funcionalidades propostas (e problemas conhecidos).

<p align="right">(<a href="#readme-top">de volta ao topo</a>)</p>



<!-- CONTRIBUTING -->
## Contribuindo

As contribuições são o que fazem a comunidade open source ser um lugar tão incrível para aprender, inspirar e criar. Quaisquer contribuições que você fizer serão muito apreciadas.

Se você tiver uma sugestão que possa melhorar este projeto, por favor, faça um fork do repositório e crie um pull request. Você também pode simplesmente abrir uma issue com a tag "enhancement" (melhoria). Não se esqueça de dar uma estrela ao projeto! Agradecemos novamente!

Faça o Fork do Projeto
Crie sua Branch de Funcionalidade (git checkout -b feature/AmazingFeature)
Comite suas Alterações (git commit -m 'Adiciona uma funcionalidade incrível')
Envie para a Branch (git push origin feature/AmazingFeature)
Abra um Pull Request

<p align="right">(<a href="#readme-top">de volta ao topo</a>)</p>

<!-- CONTACT -->
## Contato

Lucas William Martins Lima - lucaswilliamml@gmail.com - [LinkedIn][linkedin-url] - [Portfolio][portfolio-url]

<p align="right">(<a href="#readme-top">de volta ao topop</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/lucaswmlima/kayadoc.svg?style=for-the-badge
[contributors-url]: https://github.com/lucaswmlima/kayadoc/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/lucaswmlima/kayadoc.svg?style=for-the-badge
[forks-url]: https://github.com/lucaswmlima/kayadoc/network/members
[stars-shield]: https://img.shields.io/github/stars/lucaswmlima/kayadoc.svg?style=for-the-badge
[stars-url]: https://github.com/lucaswmlima/kayadoc/stargazers
[issues-shield]: https://img.shields.io/github/issues/lucaswmlima/kayadoc.svg?style=for-the-badge
[issues-url]: https://github.com/lucaswmlima/kayadoc/issues
[license-shield]: https://img.shields.io/github/license/lucaswmlima/kayadoc.svg?style=for-the-badge
[license-url]: https://github.com/lucaswmlima/kayadoc/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/https://www.linkedin.com/in/lucaswmlima/
[portfolio-url]: https://portfolio-lucaswilliam.vercel.app/#projects
[product-screenshot]: https://raw.githubusercontent.com/LucaswmLima/kayadoc/main/assets/1.png
[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org
[Django]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green
[Django-url]: https://www.djangoproject.com
[Tailwindcss]: https://img.shields.io/badge/Tailwind_CSS-grey?style=for-the-badge&logo=tailwind-css&logoColor=38B2AC
[Tailwindcss-url]: https://tailwindcss.com
[Sqlite]: https://img.shields.io/badge/SQLite-07405E?style=flat&compact=true&logo=sqlite&logoColor=white
[Sqlite-url]: https://www.sqlite.org
[Docker]: https://img.shields.io/badge/docker-257bd6?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://www.docker.com
