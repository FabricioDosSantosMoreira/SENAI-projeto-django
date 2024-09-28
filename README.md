# ⛑ Gerenciamento de EPI's
 
Projeto em Django sobre EPI's com Frontend 
O projeto tem como base um pedido que envolve gerar um site html funcional para uma empresa de "aluguel" de equipamentos de EPI. 
Para a realização do projeto tivemos que identificar os principais produto, categorias de EPI para que fossem feitas no futuro os emprestimos dos equipamentos e possiveis cargos dentro da empresa. 
O site tem como base atender a necessidade do requerimento de pedidos dos clientes, não permitindo com que mais do que a quantidade disponivel no estoque no momento preente seja requerida pelos clientes. Clientes podem escolher produto, quantidade e quando irão alugar os equipamentos. 


## Executando o Projeto

```shell
cd '.\Imersão 4\'

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

Requisitos Não Funcionais:
- O sistema deve garantir que todos os dados sejam armazenados de forma segura, garantindo a persistência dos dados
- O sistema deve ter uma interface amigável, de fácil navegação e intuitiva, respeitando normas de usabilidade.
- O sistema deve ser acessível por dispositivos móveis e desktops.
- O sistema deve garantir um tempo de resposta inferior a 2 segundos para todas as operações.
- O sistema deve ser compatível com navegadores modernos, como Chrome, Firefox e Edge.


## Participantes

- [Fabrício dos Santos Moreira] (https://github.com/FabricioDosSantosMoreira)
- [Guilherme Stadnicki da Silva] (https://github.com/guilhermestd)
- [Maria Figueiredo] (https://github.com/mariaeduardafigueiredo)
