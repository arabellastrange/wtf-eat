from flask import Flask, jsonify, request
from search import search_recipes
from flask_cors import CORS, cross_origin

app = Flask(__name__)
## allow cross-origin requests from the frontend port
CORS(
    app,
    origins=["http://localhost:5173"],
    methods=["GET"],
    supports_credentials=True
)


@app.route('/api/recipes/', methods=['GET'])
def get_data():
    ingredients = request.args.get('ingredients', '').split(',')
    return jsonify(search_recipes(ingredients).to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True, port=5174)