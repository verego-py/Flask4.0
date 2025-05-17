import os

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Flask4.0.db'
db = SQLAlchemy(app)


class DogList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    breed = db.Column(db.String(80), nullable=False)
    text = db.Column(db.Text, nullable=False)

#class User(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    name = db.Column(db.String(80))
#    email = db.Column(db.String(80))
#    password = db.Column(db.String(200))


@app.route('/id_shower')
def id_shower():
    return render_template('id_shower.html')


@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/dogs')
def dogs():
    posts = DogList.query.all()
    return render_template('dogs.html', posts = posts)


@app.route("/create", methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        breed = request.form['breed']
        text = request.form['text']
        photo = request.files['file']


        post = DogList(name=name, breed=breed, text=text)
        try:
            db.session.add(post)
            db.session.commit()
            id = post.id
            # with open('test', 'rb') as img:
            #     img.write(photo.content)
            filepath = 'C:\\Users\\user\PythonProjects\Flask4.0\static\img'
            photo.save(os.path.join(filepath, str(id) + '.png'))
            return render_template('id_shower.html', id = id)
        except:
            return "Произошла ошибка"
    else:
        return render_template('create.html')


@app.route('/in')
def ins():
     return render_template('base.html')


@app.route('/log')
def log():
     return render_template('base.html')



if __name__ == '__main__':
    app.run(debug=True)
