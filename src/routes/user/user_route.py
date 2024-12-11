from flask import Blueprint
from models import User

user_bp = Blueprint('user1',__name__) 

@user_bp.route("/", methods=["GET"])
def base_function():
    return "Esta funcionando", 200

@user_bp.route("/create", methods=["POST"])
def create_user():
    return "Usuario creado", 201

@user_bp.route("/get-all-users", methods=["GET"])
def get_all_users():    
    users = User.query.all()
    result = [user.serialize() for user in users]
    return jsonify(result), 200

@user_bp.route('/user/favorites', methods=['GET'])
def get_user_favorites():
    user_id = request.args.get('user_id')

    if not user_id:
        return jsonify({'message': 'user_id is required'}), 400

    # Filtro favoritos
    favorites = Favorite.query.filter_by(user_id=user_id).all()
    result = [favorite.serialize() for favorite in favorites]

    # Usuario sin favoritos
    if not result:
        return jsonify({'message': 'No favorites found for this user'}), 404

    return jsonify(result), 200