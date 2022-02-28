from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'


class Drinks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self) -> str:
        return f"{self.name} - {self.description}"

@app.route('/')
def index():
    return 'Hello'

@app.route('/drinks/')
def get_drinks():
    drinks = Drinks.query.all()
    print(drinks)
    out = []
    for drink in drinks:
        drink_data = {
            "name": drink.name,
            "description": drink.description,
        }
        out.append(drink_data)
    return {"drinks" : out}

@app.route('/drinks/<id>')
def get_drink(id):
    drink = Drinks.query.get_or_404(int(id))
    return {'name': drink.name, 'des': drink.description}

@app.route('/drinks', methods=['POST'])
def add_drinks():
    drink = Drinks(name = request.json['name'], description= request.json['description'])
    db.session.add(drink)
    db.session.commit()
    return {"id": drink.id}

@app.route('/drinks/<id>', methods=['DELETE'])
def delete_drinks(id):
    drink = Drinks.query.get_or_404(id)
   
    db.session.delete(drink)
    db.session.commit()
    return {"Message": "Item successfully deleted"}

@app.route('/drinks/<id>', methods = ["PUT"])
def update_drinks(id):
    drink = Drinks.query.get_or_404(id)
    drink.name = request.json['name']
    drink.description = request.json['description']
    print(drink.name)
    db.session.add(drink)
    db.session.commit()
    return {"Message": "Item successfully deleted"}
    

if __name__ == '__main__':
    app.run()