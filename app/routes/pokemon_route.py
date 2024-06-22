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
      url = f"https://pokeapi.co/api/v2/pokemon/{prediction[0]['label'].lower()}"
      description_url = f"https://pokeapi.co/api/v2/pokemon-species/{prediction[0]['label'].lower()}"
      data = requests.get(url=url).json()
      data_description = requests.get(description_url).json()
      new_pokemon = {
        "name": data['name'].capitalize(),
        "index": data['id'],
        "weight": data['weight'],
        "height": data['height'],
        "description": data_description['flavor_text_entries'][0]["flavor_text"],
        "attack": data["stats"][1]["base_stat"],
        "defense": data["stats"][2]["base_stat"],
        "sp_attack": data["stats"][3]["base_stat"],
        "sp_defense": data["stats"][4]["base_stat"],
        "speed": data["stats"][5]["base_stat"],
        "audio_url": data["cries"]["latest"],
        "sprite_url": data["sprites"]["front_default"],
        "imagen_url": data["sprites"]["other"]["official-artwork"]["front_default"],
        "tipos": [tipo["type"]["name"].upper() for tipo in data["types"]],
        "habilidades": [habilidad["ability"]["name"].replace("-", " ").title() for habilidad in data["abilities"]]
      }
      result = PokemonService.add_pokemon(new_pokemon, usuario_id)
      return jsonify(result.to_dic()), 201
    except ValueError as err:
      return jsonify({"msg": str(err)}), 400
    
  @bp.route ('/<int:pokemon_id>/detalle', methods=['GET'])
  def get_pokemon(pokemon_id):
    try:
      pokemon = PokemonService.get_pokemon(pokemon_id)
      return jsonify(pokemon.to_dic())
    except ValueError as err:
      return jsonify({"msg": str(err)}), 400