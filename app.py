from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#definir caminho do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
#iniciar conexao com o banco de dados
db = SQLAlchemy(app)
#Modelagem do banco em linhas e colunas (id,name,price,description)
class Product(db.Model):
  # o id sera um numero inteiro, e sera a chave unica
  id = db.Column(db.Integer, primary_key=True)
  # o name sera uma string de ate 120 caracteres, nao podendo ser nulo/nao informado 
  name = db.Column(db.String(120), nullable=False)
  #  price sera um numero real, tambem nao pode ser nulo
  price = db.Column(db.Float, nullable=False)
  # a description usamos um tipo Texto, que nao tem limitacao de tamanho
  description = db.Column(db.Text, nullable=True)

@app.route('/api/products/add', methods=["POST"])
def add_product():
  data = request.json
  product = Product(name=data["name"], price=data["price"], description=data.get("description", "valor default se nao informarem nada"))
  db.session.add(product)
  db.session.commit()
  return "Produto cadastrado OK"

@app.route('/')
def hello_world():
  return "Hello World!"

if __name__ == "__main__":
  app.run(debug=True)