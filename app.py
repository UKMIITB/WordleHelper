from wordle import getSuggestionResult
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET', 'POST'])
def home():
    return "Welcome to Wordle Helper API"


@app.route('/suggestion', methods=['GET', 'POST'])
def get_suggestion_result():
    ''' schema of data for this function
    {
        "guess_word": "horse",
        "guess_word_result": "yyggb",
        "iteration": 2,
        "word_list": ["abc", "def", "ghi"]
    }'''

    try:
        data = request.get_json(force=True)
        suggestion_result = getSuggestionResult(**data)
        return jsonify(
            {'suggestion_result': suggestion_result, "status": 200})

    except Exception as exception:
        return jsonify(
            {'status': 400, 'message': f"data parsing failed. Exception is: {exception}"})


if __name__ == "__main__":
    app.run()
