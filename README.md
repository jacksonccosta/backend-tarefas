# API de Gerenciamento de Tarefas
### 👨🏾‍🏫 Por Jackson Costa | PUC-RIO - Pós Graduação em Engenharia de Software

Esta é a API backend para o projeto Gerenciador de Tarefas, que faz parte do <b>MVP da Sprint 1 do curso de Engenharia de Software</b>.<br />
<h4>Aqui estou utilizando as seguintes tecnologias:</h4>
<ul style="list-style-type: none;">
    <li>
        <img align="center" alt="Rafa-Js" height="40" width="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original-wordmark.svg" />
            Linguagem de programação <b>Python</b>
    </li>
    <li>
        <img align="center" alt="Rafa-Js" height="40" width="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/sqlite/sqlite-original-wordmark.svg" />
        Banco de Dados <b>SQLite</b>
    </li>
    <li>
          <img align="center" alt="Rafa-Js" height="40" width="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/sqlalchemy/sqlalchemy-original-wordmark.svg" /> 
           ORM <b>SQLAlchemy</b></li>
    <li>
        <img align="center" alt="Rafa-Js" height="40" width="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/swagger/swagger-original-wordmark.svg" />
        API com <b>Swagger</b> documentado com o Flask
    </li>
</ul>

## Instruções de Instalação

1.  Clone este repositório.
2.  Navegue até a pasta do projeto: `cd backend-tarefas`
3.  Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```
4.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
5.  Inicialize o banco de dados (execute apenas uma vez):
    ```bash
    python database.py
    ```

## Comandos de Inicialização

Para iniciar o servidor da API, execute o seguinte comando:

```bash
python app.py
```
<img align="center" alt="Rafa-Js" height="40" width="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/postman/postman-original.svg" />
 Caso queira testar os endpoints no Postman, aqui na pasta do projeto consta o arquivo <b>PUC-MVP1.postman_collection.json</b> com as Collections que podem ser importadas no Postman.