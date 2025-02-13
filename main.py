from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

data = {
    'cookie':12345
}

db = {
    'user':"Marcos",
    'Senha': 12345
}

def set_cookie(response, key, value, max_age=None):
    response.set_cookie(key, value=str(value), max_age=max_age, secure=True, httponly=True, samesite='Lax')
    return response

def get_cookie(key):
    return request.cookies.get(key)

# @app.route('/cookie', methods=['GET'])
# def cookie():
#     response = make_response(jsonify({'success': 'Logged in'}), 200)
#     response = set_cookie(response, 'cookie', data['cookie'], max_age=100)
#     return response

# @app.route('/cookie', methods=['POST'])
# def post_cookie():
#     response = get_cookie('cookie')
#     send = {
#         'Status': 'Usuário logado',
#         'Erro':'Usuário não logado'
#     }
#     if response:
#         return jsonify(send['Status'])
#     else:
#         return jsonify(send['Erro'])
    
@app.route('/login', methods=['POST'])
def login():
    result = request.json

    if not result or not result.get('user') or not result.get('Senha'):
        return jsonify({'Erro':'Todos os compos tem que ser preenchidos'})
    
    nome = result['user']
    senha = result['Senha']

    if nome == db['user'] and senha == db['Senha']:
        return jsonify({"Success": "Login feito com sucesso"}), 200
    else:
        return jsonify({'Erro':'Dados invalidos'})


@app.route('/logout', methods=['GET'])
def logout():
    response = make_response(jsonify({'Success':'Logged out'}), 200)
    response.delete_cookie('cookie')
    return response

if __name__== '__main__':
    app.run(debug=True)