from application import app, db
from flask import request, jsonify
from application.models import FriendsCharacter

def format_character(character):
    return {
        "name": character.name,
        "age": character.age,
        "catch_phrase": character.catch_phrase
    }


@app.route("/")
def hello_world():
    return "<p>Hello world!</p>"


@app.route("/characters", methods=["POST"])
def create_character():
    data = request.json
    character = FriendsCharacter(data["name"], data["age"], data["catch_phrase"])
    db.session.add(character)
    db.session.commit()
    return jsonify(id=character.id, name=character.name, age=character.age, catch_phrase=character.catch_phrase)



@app.route("/characters", methods=["GET", "PATCH"])
def get_characters():
    if request.method == "GET":
        characters = FriendsCharacter.query.all() #gets all info from db
        characters_list = []
        for character in characters:
            characters_list.append(format_character(character))

        return {"characters": characters_list}
    elif request.method == "POST":
        id = request.view_args['id']
        character = FriendsCharacter.query.filter_by(id=id)
        data = request.json
        character.update(dict(name=data["name"], age=data["age"], catch_phrase=data["catch_phrase"]))
        db.session.commit()
        updatedCharacter = character.first()
        return jsonify(id=updatedCharacter.id, name=updatedCharacter.name, age=updatedCharacter.age, catch_phrase=updatedCharacter.catch_phrase)



@app.route("/characters/<id>", methods=["GET"])
def get_character(id):
    character = FriendsCharacter.query.filter_by(id=id).first()
    return jsonify(id=character.id, name=character.name, age=character.age, catch_phrase=character.catch_phrase)


@app.route("/characters/<id>", methods=["DELETE"])
def delete_character(id):
    character = FriendsCharacter.query.filter_by(id=id).first()
    db.session.delete(character)
    db.session.commit()
    return "Character deleted"


# @app.route("/characters/<id>", methods=["PATCH"])
# def update_character(id):
#     character = FriendsCharacter.query.filter_by(id=id)
#     data = request.json
#     character.update(dict(name=data["name"], age=data["age"], catch_phrase=data["catch_phrase"]))
#     db.session.commit()
#     updatedCharacter = character.first()
#     return jsonify(id=updatedCharacter.id, name=updatedCharacter.name, age=updatedCharacter.age, catch_phrase=updatedCharacter.catch_phrase)

