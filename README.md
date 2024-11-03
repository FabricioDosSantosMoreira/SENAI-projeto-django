# 🚧 ProTecHub | Gerenciamento de EPI's
 
O presente projeto consiste no desenvolvimento de um sistema de gerenciamento de Equipamentos de Proteção Individual (EPIs) para uma empresa de construção civil, com o objetivo de otimizar o controle e a utilização dos EPIs pelos colaboradores. O sistema tem como objetivo principal garantir que os colaboradores estejam utilizando os EPIs adequados durante a execução de suas tarefas. Para isso, o sistema permite que os colaboradores realizem a solicitação de equipamentos, com controle sobre a quantidade disponível em estoque e as datas de empréstimo e devolução.

![Página Inicial](./docs/home.png)


## 🌎 Tecnologias Utilizadas

- Python
- Django
- Django-environ
- MySQL | SQLite
- HTML5 | CSS | JS


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


## 🟢 Execução
```bash
# ⭕ OBS - Necessário ter o MAKE:
make first-run

# Ou, utilize:
cd ./ProTecHub/
poetry run python manage.py makemigrations app
poetry run python manage.py migrate
poetry run python manage.py runserver


# 🔄 Para executar o projeto novamente:
make run

# Ou, utilize:
cd ./ProTecHub/
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
