from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hola mundo desde la api de flask 🐍'

@app.route('/user', methods=['GET', 'POST', 'PUT', 'DELETE'])
def users():
    method = request.method
    if method == 'GET':
        return {
            'id': 1,
            'name': 'Juan',
            'email': 'juan@example.com'
        }
    elif method == 'POST':
        # Registrar un usuario
        json = request.get_json()
        # print(json)
        # form = request.form
        # print(form)
        # file = request.files
        # print(file)
        return json
    
@app.route('/users/<name>') # <ont:user_id>, <string:name>, <float:price>, <path:path>, <uuid:uuid>
def user(name):
    return f'Hola {name} desde la api de flask 🐍'

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    json = request.get_json()
    name = json.get('name')
    email = json.get('email')
    return {
        'id': user_id,
        'name': name,
        'email': email
    }

if __name__ == '__main__':
    app.run(debug=True)