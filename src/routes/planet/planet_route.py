from flask import Blueprint

planet_bp = Blueprint('planet1',__name__) 

@planet_bp.route("/", methods=["GET"])
def base_function():
    return "Esta funcionando", 200
