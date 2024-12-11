from flask import Blueprint

favourite_bp = Blueprint('favourite1',__name__) 

@favourite_bp.route("/", methods=["GET"])
def base_function():
    return "Esta funcionando", 200
