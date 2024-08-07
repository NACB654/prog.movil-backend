from app.models import Usuario
from app import db

class UserService:

  @staticmethod
  def create_user(data):
    name = data.get('name')
    last_name = data.get('last_name')
    nickname = data.get('nickname')
    email = data.get('email')
    password = data.get('password')

    new_user = Usuario(name=name, last_name=last_name, nickname=nickname, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()

    return new_user
  
  @staticmethod
  def get_user():
    return Usuario.query.all()
  
  @staticmethod
  def get_pokemons(id):
    return Usuario.query.get(id)
  
  @staticmethod
  def login_user(data):
      email = data.get('email')
      password = data.get('password')

      user = Usuario.query.filter_by(email=email, password=password).first()

      if user is None:
          return None

      return user
  
  @staticmethod
  def search_user(nickname):
      return Usuario.query.filter_by(nickname=nickname).first()