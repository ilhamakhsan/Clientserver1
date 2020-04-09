from flask_restful import Resource, Api
from flask import Flask, Response, json, jsonify
from flask_migrate import migrate, Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import  Marshmallow
from sqlalchemy import true

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY DATABASE_URI'] = 'mysql://root:@localhost:3306/kampus'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)

#ini adalah pertemuan 3
@app.route('/')
def hello_world():
    return 'Selamat datang'

@app.route('/admin/')
def admin():
    return 'ini adalah halaman admin'

#materi pertemuan 4
class HelloWolrd(Resource):
    def get(self):
        return {'helo':'world'}

api.add_resource(HelloWolrd, 'helloword')

#materi pertemuan 5
class User(db.Model):
    id = db.Column(db.Integer, primary_key=true)
    username = db.Column(db.String(80), unique=true)
    email = db.Column(db.String(120), unique=true)

    def _init_(self, username, email):
        self.username = username
        self.email = email

        @staticmethod
        def get_all_user():
            return  User.query.all()

class UserSchema(ma.Schema):
    class Meta:
        #Field to exposer
        fields = ('username', 'email')


if __name__ == '__main__':
    app.run()
