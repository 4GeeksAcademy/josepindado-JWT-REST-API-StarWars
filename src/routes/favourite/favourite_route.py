from flask import Blueprint
from models import Favorite

favourite_bp = Blueprint('favourite1',__name__) 

@favourite_bp.route("/", methods=["GET"])
def base_function():
    return "Esta funcionando", 200

@favourite_bp.route('/favorites/planet/<int:planet_id>', methods=['POST'])
def create_favorite_planet(planet_id):
    data = request.json
    user_id = data.get('user_id')

    if user_id is None:
        return jsonify({'message': 'The user_id field is required'}), 400

    # Verificar si existe favorito
    favorite = Favorite.query.filter_by(user_id = user_id, planet_id = planet_id, people_id = None).first()
    if favorite:
        return jsonify({'message': 'This favorite already exists'}), 400

    # Crear nuevo favorito
    new_favorite = Favorite(user_id = user_id, planet_id = planet_id, people_id = None)
    db.session.add(new_favorite)
    db.session.commit()
    
    return jsonify(new_favorite.serialize()), 200

@favourite_bp.route('/favorites/people/<int:people_id>', methods=['POST'])
def create_favorite_people(people_id):
    data = request.json
    user_id = data.get('user_id')

    if user_id is None:
        return jsonify({'message': 'The user_id field is required'}), 400

    # Verificar si existe favorito
    favorite = Favorite.query.filter_by(user_id=user_id, people_id=people_id, planet_id=None).first()
    if favorite:
        return jsonify({'message': 'This favorite already exists'}), 400

    # Crear nuevo favorito
    new_favorite = Favorite(user_id=user_id, people_id=people_id, planet_id=None)
    db.session.add(new_favorite)
    db.session.commit()
    
    return jsonify(new_favorite.serialize()), 200


@favourite_bp.route('/favorites/planet/<int:planet_id>', methods=['DELETE'])
def delete_favorite_planet(planet_id):
    user_id = request.json.get('user_id')
    favorite = Favorite.query.filter_by(user_id=user_id, planet_id=planet_id, people_id=None).first()

    if not favorite:
        return jsonify({'message': 'Favorite planet not found'}), 404

    db.session.delete(favorite)
    db.session.commit()

    return jsonify({'message': 'Favorite planet deleted successfully'}), 200

@favourite_bp.route('/favorites/people/<int:people_id>', methods=['DELETE'])
def delete_favorite_people(people_id):
    user_id = request.json.get('user_id')
    favorite = Favorite.query.filter_by(user_id=user_id, people_id=people_id, planet_id=None).first()

    if not favorite:
        return jsonify({'message': 'Favorite people not found'}), 404

    db.session.delete(favorite)
    db.session.commit()

    return jsonify({'message': 'Favorite people deleted successfully'}), 200