from flask import Flask, request, jsonify
from pico_analyzer import PICOAnalyzer

app = Flask(__name__)
pico_analyzer = PICOAnalyzer()

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    question = data.get("question", "")
    result = pico_analyzer.analyze_question(question)
    return jsonify(result)

if __name__ == '__main__':
    app.run()