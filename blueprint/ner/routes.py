from .tasks import get_entities
from flask import request, jsonify
import json
from typing import List, Dict

def validate_json_structure(data: dict, expected_structure: dict) -> bool:
    for key, expected_type in expected_structure.items():
        if key not in data: return False
        if not isinstance(data[key], expected_type): return False
    return True


def ner_api_call():
    if request.method != 'POST':
        return "Method Not Valid", 405
    
    json_data = request.get_json()
    expected_json: Dict[str, List[str]] = {
            "oraciones": list
        }

    if validate_json_structure(json_data, expected_json):
        result = get_entities(json_data)
        return jsonify(result)
    else:
        return "Json data is not valid", 400
    