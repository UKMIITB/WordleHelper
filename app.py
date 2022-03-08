from flask import Flask, request, jsonify
from wordle import getSuggestionResult

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_suggestion_result():
    ''' schema of data for this function
    {
        "guess_word": "horse",
        "guess_word_result": "yyggb",
        "iteration": 2,
        "word_list": ["abc", "def", "ghi"]
    }'''

    data = request.get_json()
    try:
        suggestion_result = getSuggestionResult(**data)
        return jsonify({'suggestion_result': suggestion_result, "status": 200})
    except Exception as exception:
        return jsonify({'status': 400, 'message': f"data parsing failed. Exception is: {exception}"})


app.run(debug=True)
