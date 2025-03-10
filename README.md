<a name="readme-top"></a>

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
    Este projeto é uma réplica das páginas do KayaDoc usando Django e TailwindCSS.
    <br />
    <a href="https://github.com/lucaswmlima/meter-read-managment-tool"><strong>Explore a documentação »</strong></a>
    <br />
    <br />
    ·
    <a href="https://github.com/lucaswmlima/meter-read-managment-tool/issues">Reportar Bug</a>
    ·
    <a href="https://github.com/lucaswmlima/meter-read-managment-tool/issues">Solicitar Recurso</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Índice</summary>
  <ol>
    <li>
      <a href="#about-the-project">Sobre o Projeto</a>
      <ul>
        <li><a href="#built-with">Tecnologias Utilizadas</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Como rodar o projeto</a>
      <ul>
        <li><a href="#prerequisites">Pré-requisitos</a></li>
        <li><a href="#installation">Como rodar o projeto</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contribuindo</a></li>
    <li><a href="#license">Licença</a></li>
    <li><a href="#contact">Contato</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
![1122](https://github.com/user-attachments/assets/db190c74-019f-471c-bb0f-62da864122d5)

<p align="right">(<a href="#readme-top">de volta ao topo</a>)</p>



### Built With
* [![node.js][Node.js]][Node.js-url]
* [![Typescript][Typescript]][Typescript-url]
* [![React.js][React.js]][React.js-url]
* [![Axios][Axios]][Axios-url]

<p align="right">(<a href="#readme-top">de volta ao topo</a>)</p>



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

6. Acesse o projeto em: http://127.0.0.1:8000/medicos (Porta padrão)


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
5. Acesse o projeto em: http://localhost:8000/medicos

6. Caso precise acessar o container, use o seguinte comando:
   ```sh
   docker-compose exec web bash
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



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

      
See the [open issues](https://github.com/lucaswmlima/meter-read-managment-tool/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Lucas William Martins Lima - lucaswilliamml@gmail.com - [LinkedIn][linkedin-url] - [Portfolio][portfolio-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/lucaswmlima/meter-read-managment-tool.svg?style=for-the-badge
[contributors-url]: https://github.com/lucaswmlima/meter-read-managment-tool/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/lucaswmlima/meter-read-managment-tool.svg?style=for-the-badge
[forks-url]: https://github.com/lucaswmlima/meter-read-managment-tool/network/members
[stars-shield]: https://img.shields.io/github/stars/lucaswmlima/meter-read-managment-tool.svg?style=for-the-badge
[stars-url]: https://github.com/lucaswmlima/meter-read-managment-tool/stargazers
[issues-shield]: https://img.shields.io/github/issues/lucaswmlima/meter-read-managment-tool.svg?style=for-the-badge
[issues-url]: https://github.com/lucaswmlima/meter-read-managment-tool/issues
[license-shield]: https://img.shields.io/github/license/lucaswmlima/meter-read-managment-tool.svg?style=for-the-badge
[license-url]: https://github.com/lucaswmlima/meter-read-managment-tool/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/https://www.linkedin.com/in/lucaswmlima/
[portfolio-url]: https://portfolio-lucaswilliam.vercel.app/#projects
[product-screenshot]: https://raw.githubusercontent.com/LucaswmLima/meter-read-managment-tool/main/assets/1.png
[HTML]: https://img.shields.io/badge/HTML-E44D26?style=for-the-badge&logo=html5&logoColor=white
[HTML-url]: https://developer.mozilla.org/pt-BR/docs/Web/HTML
[CSS]: https://img.shields.io/badge/CSS-2862E9?style=for-the-badge&logo=css3&logoColor=white
[CSS-url]: https://developer.mozilla.org/pt-BR/docs/Web/CSS
[Javascript]: https://img.shields.io/badge/Javascript-E8D44D?style=for-the-badge&logo=javascript&logoColor=black
[Javascript-url]: https://developer.mozilla.org/pt-BR/docs/Web/JavaScript
[Typescript]: https://shields.io/badge/TypeScript-3178C6?logo=TypeScript&logoColor=FFF&style=flat-square
[Typescript-url]: https://www.typescriptlang.org
[Axios]: https://img.shields.io/badge/axios.js-854195?style=for-the-badge&logo=axios&logoColor=5A29E4
[Axios-url]: https://axios-http.com/ptbr/docs/intro
[node.js]: https://img.shields.io/badge/node.js-339933?style=for-the-badge&logo=Node.js&logoColor=white
[node.js-url]: https://nodejs.org/pt
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React.js-url]: https://reactjs.org/
[Redux]: https://img.shields.io/badge/Redux-764ABC?style=for-the-badge&logo=redux&logoColor=white
[Redux-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://redux.js.org
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org
[Pandas]: https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white
[Pandas-url]: https://pandas.pydata.org
[NumPy]: https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white
[NumPy-url]: https://numpy.org
[Matplotlib]: https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black
[Matplotlib-url]: https://matplotlib.org
[Scikit-Learn]: https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white
[Scikit-Learn-url]: scikit-learn.org
[Selenium]: https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white
[Selenium-url]: https://www.selenium.dev