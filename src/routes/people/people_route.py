from flask import Blueprint

people_bp = Blueprint('people1',__name__) 

@people_bp.route("/", methods=["GET"])
def base_function():
    return "Esta funcionando", 200
