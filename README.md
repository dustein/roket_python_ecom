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

Após essas modificações, precisamos derrubar e criar as tabelas novamente, com a modelagem atualizada.

- Agora criação das rotas do cart: add, remove, checkout and clean.

Na configuração da rota de cart, usaremos do flask_login o método current_user, que é a informação do user logado no momento.

Finalizada a API, vamos ao deploy na AWS, utilizando o Elastic Beanstalk.

- Instalação da AWS Cli para podermos efetuar os comandos via terminal. No IAM do user, create acess key. No terminal, "aws configure", logar com as keys. Para ver os comandos possiveis, joga no google "aws cli beanstalk".
Agora instalou outra cli, a EB CLI, que é mais específica para o Beanstalk e vai ajudar a abstrair com menos comandos.
(git clone https://github.com/aws/aws-elastic-beanstalk-cli-setup.git)
Testar a instalação no temrinal "eb --version"
(Tive que instalar o virtualenv (sudo apt install python3-virtualenv))
- Para configurar o EB, há uma exigência. O nome do arquivo tem que ser "application.py", bem como a variável que instancia "app" tem que se chamar "application". POrtanto tive que alterar esses nomes na API.
https://docs.aws.amazon.com/pt_br/elasticbeanstalk/latest/dg/create-deploy-python-flask.html

- No terminal usamos a EB CLI:
"eb init -p python-3.11 flask-ecomm-api --region us-east-1"
Em seguida, criamos o ambiente "eb create flask-env-dev" colocamos o -dev para lembrar que estamos em um ambiente de desenvolvimento.
A AWS vai demorar uns 5 minutos e criar todos os recursos para o deploy, e quando terminar podemos dar CTRL+C para sair.

Para abrir o servidor que fizemos o deploy, "eb open flask-ecomm-api"
Para fazer update ou alterar a aplicação já feito o deploy, usamos "eb deploy flask-ecomm-ap"

Para FINALIZAR a aplicação (lembre que AWS tem os limites free tier)
"eb terminate flask-env-dev" e todos os recursos serão desprovisionados.








4.41.00

lost kittys
