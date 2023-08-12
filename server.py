from flask import (
    Flask,
)
from blueprint.ner import ner_bp
app = Flask(__name__)
app.register_blueprint(ner_bp, url_prefix='/ner')


@app.route('/')
def home():
    return "Welcome to Named Entity Recogntion"



if __name__ == '__main__':
    app.run(debug=True, port=80)