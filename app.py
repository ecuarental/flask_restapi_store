"""Flask app definition."""
from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from resources.item import Item, ItemList
from resources.store import Store, StoreList
from resources.user import UserRegister
from security import authenticate, identity


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://{}:{}@{}/{}?host={}?port={}".format(
        "designwo_user",
        "Asdf1234",
        "127.0.0.1",
        "designwo_flaskstoreapi",
        "www.designworkstudio.org",
        "3306")
# mysql+pymysql://sylvain:passwd@localhost/db?host=localhost?port=3306
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'jose'
api = Api(app)





jwt = JWT(app, authenticate, identity)


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')


@app.route('/')
def home():
    """Homepage."""
    return 'Hello world!'


if __name__ == '__main__':
    from db import db  # noqa
    db.init_app(app)

    @app.before_first_request
    def create_tables():
        """Create tables in the db."""
        db.create_all()
    
    app.run()  # important to mention debug=True
