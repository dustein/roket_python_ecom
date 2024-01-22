from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

#definir caminho do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
#iniciar conexao com o banco de dados
db = SQLAlchemy(app)

#Modelagem do banco em linhas e colunas
#Modelagem Usuarios
class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(10), nullable=False, unique=True)
  password = db.Column(db.String(20), nullable=False)

#Modelagem Produtos
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
  if 'name' in data and 'price' in data:
    product = Product(name=data["name"], price=data["price"], description=data.get("description", "valor default se nao informarem nada"))
    db.session.add(product)
    db.session.commit()
    return jsonify({"message":"Produto cadastrado OK"}), 200
  # se o post nao informar o nome e preco, retorna msg de erro 400
  return jsonify({"message":"product data is invalid or not informed"}), 400

@app.route('/api/products/delete/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
  # recupera o produto buscando pelo id
  product = Product.query.get(product_id)
  if product:
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message":"Product deleted"})
  return jsonify({"message":"This ID does not exist"}), 404
  # apagar da base de dados o produto encontrado

# retorna resultado busca por id
@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product_details(product_id):
  product = Product.query.get(product_id)
  if product:
    return jsonify({
      "id": product.id,
      "name": product.name,
      "price": product.price,
      "description": product.description
    }), 200
  return jsonify({"message":"This ID does not exist"}), 404
  
# modifica item
@app.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
  product = Product.query.get(product_id)
  
  if not product:
    return jsonify({"message": "Product not found in database"}), 404
  
  data = request.json
  if 'name' in data:
    product.name = data['name']
  if 'price' in data:
    product.price = data['price']
  if 'description' in data:
    product.description = data['description']

  db.session.commit()
  return jsonify({"message":"Product updated OK!"})

# listar todos os produtos cadastrados
@app.route('/api/products')
def get_products():
  products = Product.query.all()
  products_list = []

  for product in products:
    product_data = {
      "id": product.id,
      "name": product.name,
      "price": product.price,
      # vamos deixar sem a descricao, quem quiser detalhe busca o produto especifico
      # "description": product.description
    }
    products_list.append(product_data)

  return products_list


if __name__ == "__main__":
  app.run(debug=True)