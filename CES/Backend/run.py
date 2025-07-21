from app import create_app
from flask import jsonify

app = create_app()

@app.route('/')
def index():
    return jsonify({'message': 'Welcome to the UEAB Emergency API!'})

if __name__ == '__main__':
    app.run(debug=True)