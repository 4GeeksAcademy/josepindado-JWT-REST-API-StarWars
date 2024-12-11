from flask import Blueprint

user_bp = Blueprint('user1',__name__) 

@user_bp.route("/", methods=["GET"])
def base_function():
    return "Esta funcionando", 200

@user_bp.route("/create", methods=["POST"])
def create_user():
    return "Usuario creado", 201

@user_bp.route("/get-all-users", methods=["GET"])
def get_all_users():
    return "Usuarios: ", 200