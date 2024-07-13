from flask import Blueprint, request, jsonify
from app.services import PokemonService
import requests

class PokemonRoute:
  bp = Blueprint('pokemon_routes', __name__, url_prefix='/pokemons')

  @bp.route ('/identificar/<int:usuario_id>', methods=['POST'])
  def identify_pokemon(usuario_id):
    data = request.files['file']

    try:
      prediction = PokemonService.identify_pokemon(data)
      new_pokemon = PokemonService.add_pokemon(prediction, usuario_id)

      if type(new_pokemon) == "String":
        return jsonify({"msg": new_pokemon})
      else:
        return jsonify(new_pokemon.to_dic()), 201
      
    except ValueError as err:
      return jsonify({"msg": str(err)}), 400
    
  @bp.route ('/<int:pokemon_id>/detalle', methods=['GET'])
  def get_pokemon(pokemon_id):
    try:
      pokemon = PokemonService.get_pokemon(pokemon_id)
      return jsonify(pokemon.to_dic())
    except ValueError as err:
      return jsonify({"msg": str(err)}), 400