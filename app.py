from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#definir caminho do banco de dados
app.config['SQLAlchemy_DATABASE_URI'] = 'sqlite:///ecommerce.db'
#iniciar conexao com o banco de dados
db = SQLAlchemy(app)
#Modelagem do banco em linhas e colunas



@app.route('/')
def hello_world():
  return "Hello World!"

if __name__ == "__main__":
  app.run(debug=True)