# ⛑ Gerenciamento de EPI's
 
O presente projeto consiste no desenvolvimento de um sistema de gerenciamento de Equipamentos de Proteção Individual (EPIs) para uma empresa de construção civil, com o objetivo de otimizar o controle e a utilização dos EPIs pelos colaboradores. O sistema tem como objetivo principal garantir que os colaboradores estejam utilizando os EPIs adequados durante a execução de suas tarefas. Para isso, o sistema permite que os colaboradores realizem a solicitação de equipamentos, com controle sobre a quantidade disponível em estoque e as datas de empréstimo e devolução.

Funcionalidades Principais:
- Cadastro de EPI's
- Cadastro Usuário
- Cadastro de Empréstimos

![Página Inicial](./docs/home.png)


## Executando o Projeto

```shell
cd '.\Imersão 5\'

-> Criando e executando as migrações:
python manage.py makemigrations app
python manage.py migrate

-> Executando
python manage.py runserver


-> Ou
docker-compose up --build
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

- [Fabrício dos Santos Moreira] (https://github.com/FabricioDosSantosMoreira)
- [Guilherme Stadnicki da Silva] (https://github.com/guilhermestd)
- [Maria Eduarda Figueiredo] (https://github.com/mariaeduardafigueiredo)
