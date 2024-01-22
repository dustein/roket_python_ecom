Projeto backend loja virtual propaganda curso Python da Rocketseat.
Utilizando Flask e SQLite.

- Instalando dependências. Ou utiliza o arquivo requirements.txt ("pip3 install -r requirements.txt") ou "pip3 install Flask==2.3.0" por exemplo.

- Depois da modelagem, vamos criar o banco de dados.
No terminal: "flask shell" para abrir o prompt de comando, então "db.create_all()" e sera criada o bando de dados conforme a tabela de modelagem. Após o comando, se não tiver nenhuma mensagem de retorno, é porque não deu erro e o banco foi criado.
  Em seguida, "db.session.commit()". A session é a propriedade do db que armazena a conexão com o bando de dados, e o método commit é o que vai efetivar as mudanças feitas na tabela, se não der commit, não enviará a mudança.
  Em seguida, "exit()"

- Para modelagem do User e login de acesso à API, vamos usar a biblioteca flask_login

- Para permitir acesso da API por aplicacoes externas, usaremos o CORS "from flask_cors import CORS"

- Passamos a configurar o cadastro e acesso de Users. Assim, a tabela do banco que estavamos usando, vamos descartar, "db.drop_all()", e após finalizar o model do User, de novo vamos "db.create.all()" e posteriormente para aplicar, "db.session.commit()". E depois exit().
Agora passamos a ter 2 tabelas no banco, uma do Users e outra do Products.

Na aula, ao invés de criar a rota para cadastrar o User, ensinou a criar usando o flask shell.
"user = User(username="admin", password="12345")" para criar o user, depois "db.session.add(user)" e finalmente "db.session.commit()".


2.33.00