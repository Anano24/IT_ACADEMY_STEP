from flask import Flask, render_template, request, redirect, url_for
from model import db, Cars
from flask_migrate import Migrate


app = Flask(__name__)


HOST = 'localhost'
PORT = 5432
DATABASE = 'flask_db'
USER = 'postgres'
PASSWORD = '...anano24'

app.secret_key = 'stjkhlhyggfddcvj'
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)



@app.route('/', methods=['GET'])
def index():
    all_data = Cars.query.all()

    return render_template('index.html', cars = all_data)



@app.route('/insert', methods=['POST'])
def insert():

    if request.method == 'POST':

        manufacturer = request.form['manufacturer']
        model = request.form['model']
        instock = request.form['instock']
        price = request.form['price']

        car = Cars(manufacturer, model, instock, price)

        db.session.add(car)
        db.session.commit()

        return redirect(url_for('index'))



@app.route('/delete/<id>/', methods=['GET', 'POST'])
def delete(id):

    car = Cars.query.get(id)
    
    if car:
        db.session.delete(car)
        db.session.commit()

    return redirect(url_for('index'))


@app.route('/update/<id>', methods=['GET', 'POST'])
def update(id):

    car = Cars.query.get(id)
    if request.method == 'POST':
        if car:
            car.manufacturer = request.form['manufacturer']
            car.model = request.form['model']
            car.instock = request.form['instock']
            car.price = request.form['price']

            db.session.commit()

    return redirect(url_for('index'))






if __name__ == '__main__':

    with app.app_context():
        db.create_all()

    app.run(debug=True)