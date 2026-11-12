from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/ingredients', methods=['GET'])
def get_data():
    data = {'key': 'value'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)