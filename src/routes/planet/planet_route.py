from flask import Blueprint
from models import Planet

planet_bp = Blueprint('planet1',__name__) 

@planet_bp.route("/", methods=["GET"])
def base_function():
    return "Esta funcionando", 200

@planet_bp.route('/planet', methods=['GET'])
def get_planets():

    planets = Planet.query.all()
    result = [planet.serialize() for planet in planets]

    return jsonify(result), 200


@planet_bp.route('/planet/<int:id>', methods=['GET'])
def get_planet(id):

    planet = Planet.query.get(id)
    if planet is None :
        return jsonify({'message':'404 do not exist'}), 404
    #result = [planet.serialize() for planet in planets]

    return jsonify(planet.serialize()), 200
