from app.models import Pokemon, Tipo, Habilidad, Usuario, Ruta
from app import db
import requests

API_URL = "https://api-inference.huggingface.co/models/imjeffhi/pokemon_classifier"
headers = {"Authorization": "Bearer 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"}

class PokemonService:

  @staticmethod
  def add_pokemon(prediction, user_id):
    if len(prediction) > 0:
      url = f"https://pokeapi.co/api/v2/pokemon/{prediction[0]['label'].lower()}"
      description_url = f"https://pokeapi.co/api/v2/pokemon-species/{prediction[0]['label'].lower()}"
      generation_url = f"https://pokeapi.co/api/v2/pokemon-species/{prediction[0]['label'].lower()}"

      data = requests.get(url=url).json()
      data_description = requests.get(description_url).json()
      data_generation = requests.get(generation_url).json()['generation']['name']
      data_locations = requests.get(data['location_area_encounters']).json()

      filtered_locations = PokemonService.get_locations(data_locations, data_generation)

      new_prediction = {
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
        "habilidades": [habilidad["ability"]["name"].replace("-", " ").title() for habilidad in data["abilities"]],
        "rutas": [ruta["name"].replace("-", " ").title() for ruta in filtered_locations]
      }
      
      new_pokemon = Pokemon(
              name=new_prediction.get('name'),
              index=new_prediction.get('index'),
              weight=new_prediction.get('weight'),
              height=new_prediction.get('height'),
              description=new_prediction.get('description'),
              attack=new_prediction.get('attack'),
              defense=new_prediction.get('defense'),
              sp_attack=new_prediction.get('sp_attack'),
              sp_defense=new_prediction.get('sp_defense'),
              speed=new_prediction.get('speed'),
              audio_url=new_prediction.get('audio_url'),
              sprite_url=new_prediction.get('sprite_url'),
              imagen_url=new_prediction.get('imagen_url')
          )

      tipo_nombres = new_prediction.get('tipos', [])
      for tipo_nombre in tipo_nombres:
        tipo = Tipo.query.filter_by(name=tipo_nombre).first()
        if tipo:
          new_pokemon.tipos.append(tipo)

      habilidad_nombres = new_prediction.get('habilidades', [])
      for habilidad_nombre in habilidad_nombres:
        habilidad = Habilidad.query.filter_by(name=habilidad_nombre).first()
        if habilidad:
          new_pokemon.habilidades.append(habilidad)

      ruta_nombres = new_prediction.get('rutas', [])
      for ruta_nombre in ruta_nombres:
        ruta = Ruta.query.filter_by(name=ruta_nombre).first()
        if ruta:
          new_pokemon.rutas.append(ruta)

      user = Usuario.query.get(user_id)
      user.pokemons.append(new_pokemon)
      
      # db.session.add(new_pokemon)
      # db.session.commit()

      return new_pokemon
    else:
      return "Error en la conexion. Vuelve a intentar mas tarde"
  
  @staticmethod
  def identify_pokemon(image):
    data = image.read()
    response = requests.post(API_URL, headers=headers, data=data)
    
    return response.json()
  
  @staticmethod
  def get_pokemon(id):
    return Pokemon.query.get(id)
  
  def get_locations(locations, generation):
    regions = {
      'generation-i': 'kanto',
      'generation-ii': 'johto',
      'generation-iii': 'hoenn',
      'generation-iv': 'sinnoh',
      'generation-v': 'unova',
      'generation-vi': 'kalos'
    }
    filtered_location = []

    for location in locations:
      area_url = location['location_area']['url']
      area = requests.get(area_url).json()
      
      location_url = area['location']['url']
      location = requests.get(location_url).json()

      if location['region']['name'] == regions[generation]:
        filtered_location.append(location)

    return filtered_location
