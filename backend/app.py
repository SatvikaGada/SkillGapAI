from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to SkillGapAI API!"})

if __name__ == '__main__':
    app.run(debug=True)
