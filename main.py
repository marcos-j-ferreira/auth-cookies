from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

data = {
    'cookie':12345
}
db = { 
    'users':[
        {   
    'id': 1,
    'user':"Marcos",
    'senha': 12345}
]}

def set_cookie(response, key, value, max_age=None):
    response.set_cookie(key, value=str(value), max_age=max_age, secure=True, httponly=True, samesite='Lax')
    return response

def get_cookie(key):
    return request.cookies.get(key)
    
@app.route('/login', methods=['POST', 'GET', 'DELETE'])
def login():

    result = request.json
    if request.method == 'GET':
        cookie = get_cookie('cookie')
    
        if cookie:
            return jsonify({"Status":"Usuário já logado"})
        else:
            return jsonify({"Satus":"Usuário não logado"})
    
    if request.method == 'DELETE':
        response = make_response(jsonify({'Success': 'Logged out'}), 200)
        response.delete_cookie('cookie')
        return response
    
    if not result or not result.get('user') or not result.get('senha'):
        return jsonify({'Erro':'Todos os compos tem que ser preenchidos'})

    nome = result['user']
    senha = result['senha']

    user = next((u for u in db['users'] if u['user'] == nome and u['senha'] == senha), None)

    if user:
        response = make_response(jsonify({'success': 'Logged in'}), 200)
        response = set_cookie(response, 'cookie', data['cookie'], max_age=100)
        return response, 200
    else:
        return jsonify({'Erro':'Dados invalidos'})
    
@app.route('/cadastro', methods=['POST'])

def cadastro():
    
    result = request.json

    if not result or not result.get('user') or not result.get('senha'):
        return jsonify({'Erro':'Todos os Campos tem que ser preenchido'})
    
    user = next((u for u in db['users'] if u['user'] == result['user']), None)

    if user:
        return jsonify({"Erro":"Nome já cadastrado"})
    
    nome = result['user']
    senha = result['senha']

    try:
        new_id = len(db['users']) + 1
        
        db['users'].append({ 
            'id': new_id,
            'user':nome,
            'senha': senha
        })
    except Exception as e :
        return jsonify({"Erro":"Erro ao adicionar dados"})
    finally:
        return jsonify(db)

if __name__== '__main__':
    app.run(debug=True)