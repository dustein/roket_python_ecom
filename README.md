Projeto backend loja virtual propaganda curso Python da Rocketseat.
Utilizando Flask e SQLite.

- Instalando dependências. Ou utiliza o arquivo requirements.txt ("pip3 install -r requirements.txt") ou "pip3 install Flask==2.3.0" por exemplo.

- Depois da modelagem, vamos criar o banco de dados.
No terminal: "flask shell" para abrir o prompt de comando, então "db.create_all()" e sera criada o bando de dados conforme a tabela de modelagem. Após o comando, se não tiver nenhuma mensagem de retorno, é porque não deu erro e o banco foi criado.
  Em seguida, "db.session.commit()". A session é a propriedade do db que armazena a conexão com o bando de dados, e o método commit é o que vai efetivar as mudanças feitas na tabela, se não der commit, não enviará a mudança.
  Em seguida, "exit()"

  