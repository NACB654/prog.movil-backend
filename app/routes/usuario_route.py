from flask import Blueprint, request, jsonify
from app.services import UserService

class UserRoute:
  bp = Blueprint('usuario_routes', __name__, url_prefix='/usuarios')

  @bp.route('/', methods=['GET'])
  def get_users():
    users = UserService.get_user()
    return jsonify([user.to_dic() for user in users])

  @bp.route ('/', methods=['POST'])
  def create_user():
    data = request.get_json()

    try:
      new_user = UserService.create_user(data)
      return jsonify(new_user.to_dic()), 201
    except ValueError as err:
      return jsonify({"msg": str(err)}), 400