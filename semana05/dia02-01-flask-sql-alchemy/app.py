from flask import Flask
from flask_sqlalchemy import SQLAlchemy # type: ignore
from sqlalchemy import Column, Integer, String, DateTime, func # type: ignore

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Julinho06@localhost:5432/flask_sqlalchemy'
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=func.now())

    def __str__(self):
        return self.name

with app.app_context():
    db.create_all()

@app.route('/users')
def users():
    try:
        users = User.query.all() # SELECT * FROM users
        users_list = []
        for user in users:
            users_list.append({
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'created_at': str(user.created_at)
            })
        return users_list
    except Exception as e:
        return {
            'message': str(e)
        }

@app.route('/')
def home():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)