# 🚧 ProTecHub | Gerenciamento de EPI's
 
O presente projeto consiste no desenvolvimento de um sistema de gerenciamento de Equipamentos de Proteção Individual (EPIs) para uma empresa de construção civil, com o objetivo de otimizar o controle e a utilização dos EPIs pelos colaboradores. O sistema tem como objetivo principal garantir que os colaboradores estejam utilizando os EPIs adequados durante a execução de suas tarefas. Para isso, o sistema permite que os colaboradores realizem a solicitação de equipamentos, com controle sobre a quantidade disponível em estoque e as datas de empréstimo e devolução.


## 🌎 Tecnologias Utilizadas

- Python
- Django | Pytz
- MySQL  | SQLite3
- HTML5  | CSS | JS


## 🖼 Galeria
|                                                                   |                                                                     |
|-------------------------------------------------------------------|---------------------------------------------------------------------|
| ![Home](./docs/img/01%20-%20Home.png)                             | ![Interno](./docs/img/02%20-%20Interno.png)                         |
| ![Usuários](./docs/img/03%20-%20Tabela%20de%20Usuários.png)       | ![Equipamentos](./docs/img/04%20-%20Tabela%20de%20Equipamentos.png) |
| ![Empréstimos](./docs/img/05%20-%20Tabela%20de%20Empréstimos.png) | ![Histórico](./docs/img/06%20-%20Tabela%20de%20Histórico.png)       |


## ⚙ Instalação

### 🔹 Clone o repositório
```bash
git clone https://github.com/FabricioDosSantosMoreira/SENAI-projeto-django.git
```

### 🔹 Instale as dependências

```bash
# ⭕ OBS - Necessário ter o MAKE:
make install  

# Ou, utilize:
pip install poetry
cd ./ProTecHub/
poetry install
```


## 🔹 Configure o MySQL (Opcional)
```bash
# ⭕ OBS - Necessário ter o MySQL:
Crie um banco de dados localmente usando o `MySQL` e contendo:
- NAME = `gerenciamento`
- HOST = `localhost`
- PORT = `3306`
- USER = `root`
- PASS = `123456`

# Ou, se preferir você pode mudar as configurações em: `./ProTecHub/projeto/settings.py`.
```


## 🟢 Execução
```bash
# ⭕ OBS - Necessário ter o MAKE:

make first-sqlite-run  # Executa usando o SQLite3 built-in do Django

make first-mysql-run  # Executa utilizando o MySQL configurado


# Ou, utilize:
set USE_SQLITE=True  # Pode ser False ou True, caso seja True usará o SQLite3. Caso Falso usará o MySQL.
cd ./ProTecHub/
poetry run python manage.py migrate
poetry run python manage.py runserver
```


## Requisitos Funcionais e Não Funcionais

Requisitos Funcionais:
- O sistema deve permitir o cadastro de novos colaboradores, EPI’s e empréstimos.
- O sistema deve permitir atualizar colaboradores, EPI’s e empréstimos.
- O sistema deve permitir deletar colaboradores, EPI’s e empréstimos.
- O sistema deve permitir cadastrar um empréstimo de EPIs a um colaborador.
- O sistema deve permitir o registro da devolução de EPIs, alterando o status do empréstimo.
- O sistema deve permitir que somente colaboradores possam criar empréstimos

Requisitos Não Funcionais:
- O sistema deve garantir que todos os dados sejam armazenados de forma segura, garantindo a persistência dos dados
- O sistema deve ter uma interface amigável, de fácil navegação e intuitiva, respeitando normas de usabilidade.
- O sistema deve ser acessível por dispositivos móveis e desktops.
- O sistema deve garantir um tempo de resposta inferior a 2 segundos para todas as operações.
- O sistema deve ser compatível com navegadores modernos, como Chrome, Firefox e Edge.


## Participantes

- [Fabrício dos Santos Moreira]  (https://github.com/FabricioDosSantosMoreira)
- [Maria Eduarda Figueiredo]     (https://github.com/mariaeduardafigueiredo)
- [Guilherme Stadnicki da Silva] (https://github.com/guilhermestd)


## 💡 Contribuição

Sinta se livre para contribuir com qualquer sugestão, correção ou dicas. Basta abrir um pull request!


## 📃 Licença

O projeto é licensiado sob a licença do MIT. Veja a [Licença](LICENSE/) para mais informações.
