from flask import Blueprint
from models import Favourite

favourite_bp = Blueprint('favourite1',__name__) 

@favourite_bp.route("/", methods=["GET"])
def base_function():
    return "Esta funcionando", 200

@favourite_bp.route('/favourites/planet/<int:planet_id>', methods=['POST'])
def create_favourite_planet(planet_id):
    data = request.json
    user_id = data.get('user_id')

    if user_id is None:
        return jsonify({'message': 'The user_id field is required'}), 400

    # Verificar si existe favorito
    favourite = Favourite.query.filter_by(user_id = user_id, planet_id = planet_id, people_id = None).first()
    if favourite:
        return jsonify({'message': 'This favourite already exists'}), 400

    # Crear nuevo favorito
    new_favourite = Favourite(user_id = user_id, planet_id = planet_id, people_id = None)
    db.session.add(new_favourite)
    db.session.commit()
    
    return jsonify(new_favourite.serialize()), 200

@favourite_bp.route('/favourites/people/<int:people_id>', methods=['POST'])
def create_favourite_people(people_id):
    data = request.json
    user_id = data.get('user_id')

    if user_id is None:
        return jsonify({'message': 'The user_id field is required'}), 400

    # Verificar si existe favorito
    favourite = Favourite.query.filter_by(user_id=user_id, people_id=people_id, planet_id=None).first()
    if favourite:
        return jsonify({'message': 'This favourite already exists'}), 400

    # Crear nuevo favorito
    new_favourite = Favourite(user_id=user_id, people_id=people_id, planet_id=None)
    db.session.add(new_favourite)
    db.session.commit()
    
    return jsonify(new_favourite.serialize()), 200


@favourite_bp.route('/favourites/planet/<int:planet_id>', methods=['DELETE'])
def delete_favourite_planet(planet_id):
    user_id = request.json.get('user_id')
    favourite = Favourite.query.filter_by(user_id=user_id, planet_id=planet_id, people_id=None).first()

    if not favourite:
        return jsonify({'message': 'Favourite planet not found'}), 404

    db.session.delete(favourite)
    db.session.commit()

    return jsonify({'message': 'Favourite planet deleted successfully'}), 200

@favourite_bp.route('/favourites/people/<int:people_id>', methods=['DELETE'])
def delete_favourite_people(people_id):
    user_id = request.json.get('user_id')
    favourite = Favourite.query.filter_by(user_id=user_id, people_id=people_id, planet_id=None).first()

    if not favourite:
        return jsonify({'message': 'Favourite people not found'}), 404

    db.session.delete(favourite)
    db.session.commit()

    return jsonify({'message': 'Favourite people deleted successfully'}), 200