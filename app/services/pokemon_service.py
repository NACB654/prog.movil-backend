from app.models import Pokemon, Tipo, Habilidad, Usuario
from app import db
import requests

API_URL = "https://api-inference.huggingface.co/models/imjeffhi/pokemon_classifier"
headers = {"Authorization": "Bearer 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"}

class PokemonService:

  @staticmethod
  def add_pokemon(data, user_id):
    new_pokemon = Pokemon(
            name=data.get('name'),
            index=data.get('index'),
            weight=data.get('weight'),
            height=data.get('height'),
            description=data.get('description'),
            attack=data.get('attack'),
            defense=data.get('defense'),
            sp_attack=data.get('sp_attack'),
            sp_defense=data.get('sp_defense'),
            speed=data.get('speed'),
            audio_url=data.get('audio_url'),
            sprite_url=data.get('sprite_url'),
            imagen_url=data.get('imagen_url')
        )

    tipo_nombres = data.get('tipos', [])
    for tipo_nombre in tipo_nombres:
      tipo = Tipo.query.filter_by(name=tipo_nombre).first()
      if tipo:
        new_pokemon.tipos.append(tipo)

    habilidad_nombres = data.get('habilidades', [])
    for habilidad_nombre in habilidad_nombres:
      habilidad = Habilidad.query.filter_by(name=habilidad_nombre).first()
      if habilidad:
        new_pokemon.habilidades.append(habilidad)

    user = Usuario.query.get(user_id)
    user.pokemons.append(new_pokemon)
    
    db.session.add(new_pokemon)
    db.session.commit()

    return new_pokemon
  
  @staticmethod
  def identify_pokemon(image):
    data = image.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()
  
  @staticmethod
  def get_pokemon(id):
    return Pokemon.query.get(id)