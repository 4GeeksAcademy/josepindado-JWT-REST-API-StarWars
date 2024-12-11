from flask import Blueprint
from models import People

people_bp = Blueprint('people1',__name__) 

@people_bp.route("/", methods=["GET"])
def base_function():
    return "Esta funcionando", 200

@people_bp.route('/people', methods=['GET'])
def get_peoples():

    peoples = People.query.all()
    result = [people.serialize() for people in peoples]

    return jsonify(result), 200


@people_bp.route('/people/<int:id>', methods=['GET'])
def get_people(id):

    people = People.query.get(id)
    if people is None :
        return jsonify({'message':'404 do not exist'}), 404

    return jsonify(people.serialize()), 200