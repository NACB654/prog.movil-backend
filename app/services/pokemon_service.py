from app.models import Pokemon
from app import db

class UserService:

  @staticmethod
  def add_pokemon(data):
    name = data.get("name")
    index = data.get("index")
    weight = data.get("weight")
    height = data.get("height")
    description = data.get("description")
    attack = data.get("attack")
    defense = data.get("defense")
    sp_attack = data.get("sp_attack")
    sp_defense = data.get("sp_defense")
    speed = data.get("speed")
    audio_url = data.get("audio_url")
    sprite_url = data.get("sprite_url")
    imagen_url = data.get("imagen_url")

    new_pokemon = Pokemon(
      name=name,
      index=index,
      weight=weight,
      height=height,
      description=description,
      attack=attack,
      defense=defense,
      sp_attack=sp_attack,
      sp_defense=sp_defense,
      speed=speed,
      audio_url=audio_url,
      sprite_url=sprite_url,
      imagen_url=imagen_url
    )
    db.session.add(new_pokemon)
    db.session.commit()

    return new_pokemon
  
  @staticmethod
  def get_pokemons():
    return Pokemon.query.all()