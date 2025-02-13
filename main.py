from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

data = {
    'cookie':12345
}

def set_cookie(response, key, value, max_age=None):
    response.set_cookie(key, value=str(value), max_age=max_age, secure=True, httponly=True, samesite='Lax')
    return response

def get_cookie(key):
    return request.cookies.get(key)


@app.route('/cookie', methods=['GET'])
def cookie():

    response = make_response(jsonify({'success': 'Logged in'}), 200)
    response = set_cookie(response, 'cookie', data['cookie'], max_age=100)
    
    return response




if __name__== '__main__':
    app.run(debug=True)