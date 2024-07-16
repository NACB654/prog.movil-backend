from flask import Blueprint, request, jsonify
from app.services import UserService

class UserRoute:
  bp = Blueprint('usuario_routes', __name__, url_prefix='/usuarios')

  @bp.route('/', methods=['GET'])
  def get_users():
    users = UserService.get_user()
    return jsonify([user.to_dic() for user in users])

  @bp.route('/register', methods=['POST'])
  def create_user():
        data = request.get_json()
        try:
            new_user = UserService.create_user(data)
            return jsonify(new_user.to_dic()), 201
        except ValueError as err:
            return jsonify({"msg": str(err)}), 400
    
  @bp.route ('/<int:usuario_id>/pokemons', methods=['GET'])
  def get_pokemons(usuario_id):
    try:
      results = UserService.get_pokemons(usuario_id)
      pokemons = [result.to_dic() for result in results.pokemons]
      pokemons = sorted(pokemons, key=lambda x : x['index'])

      return jsonify(pokemons)
    except ValueError as err:
      return jsonify({"msg": str(err)}), 400
    
  @bp.route('/login', methods=['POST'])
  def login_user():
      data = request.get_json()

      user = UserService.login_user(data)
      if user is None:
          return jsonify({"error": "Invalid email or password"}), 401

      return jsonify(user.to_dic()), 200
  
  @bp.route('/search', methods=['GET'])
  def search_user():
      nickname = request.args.get('nickname')
      if not nickname:
          return jsonify({"error": "Nickname is required"}), 400

      user = UserService.search_user(nickname)
      if not user:
          return jsonify({"error": "User not found"}), 404

      return jsonify(user.to_dic())