from flask import Blueprint
from .routes import ner_api_call

ner_bp = Blueprint('ner_bp', __name__)
ner_bp.add_url_rule('/api', view_func=ner_api_call, methods=['POST'])