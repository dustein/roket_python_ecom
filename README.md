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

Para autenticar, usa a lib Flask Login, com o modulo login_user, e LoginManager.
No loginManager, estabelecemos a login.view, que é a rota de acesso para login que estabelecemos na api. E vai ser necessário uma secret key, que definimos a que quisermos e informamos num app.config['SECRET KEY'].
Após efetuar o login, podemos ver no headers que foi criado um cookie de autenticação, e assim constatamos que funcionou.
Finalmente, protegemos as rotas que quisermos com o login_required (@login_required).
E, ainda, configurar uma função chamada user_loader. Assim, toda vez que fizermos uma requisição numa rota protegida pelo @login_required, o flask login vai precisar recuperar o usuário que está acessando a rota, e ele assim o fará consultando o @user_loader.

Configuramos agora também a rota de logout, usando o logout_user da mesma lib.

- Próximo passo é criar o carrinho de compras, que será um banco de dados que receberá dados dos modelos Products e do Users.
Nessa tabela de checkout, vamos associar o id do model user, com o método ForeingKey, que fará refer6encia a chave do model User e Products.
E vamos modificar o modelo de User para incluir o cart (carrinho) fazendo uma associação com a tebela CartItem.
A propriedade backref serve para associar um item ao carrinho, e através do user, consegue recuperar o item do cart.
Por fim, o método lazy é para que não sejam recuperados a cada vez que carregar/recuperar informação do user, como para checar autenticação, todos os objetos do carrinho, o que causaria lentidão no processo quando houver uma quantidade muito grande de itens. Assim, o lazy fará com que as informações referentes aos itens no carrinho sejam carregadas apenas quando o user acessar algum processo específico que precise carregar estas informações.



2.33.00