from flask import Blueprint, request, jsonify
from app.services import FriendService

class FriendRoute:
    bp = Blueprint('friend_routes', __name__, url_prefix='/friends')

    @bp.route('/add_friend', methods=['POST'])
    def add_friend():
        data = request.get_json()
        current_user_id = data.get('current_user_id')
        friend_id = data.get('friend_id')

        if not current_user_id or not friend_id:
            return jsonify({"error": "Missing user IDs"}), 400

        try:
            response = FriendService.add_friend(current_user_id, friend_id)
            return jsonify(response), 201
        except ValueError as err:
            return jsonify({"error": str(err)}), 404

    @bp.route('/get_friends', methods=['GET'])
    def get_friends():
        current_user_id = request.args.get('current_user_id')
        if not current_user_id:
            return jsonify({"error": "Missing user ID"}), 400

        try:
            friends = FriendService.get_friends(current_user_id)
            return jsonify(friends), 200
        except ValueError as err:
            return jsonify({"error": str(err)}), 404

    @bp.route('/delete_friend', methods=['DELETE'])
    def delete_friend():
        data = request.get_json()
        current_user_id = data.get('current_user_id')
        friend_id = data.get('friend_id')
        if not current_user_id or not friend_id:
            return jsonify({"error": "Missing user IDs"}), 400

        try:
            response = FriendService.delete_friend(current_user_id, friend_id)
            return jsonify(response), 200
        except ValueError as err:
            return jsonify({"error": str(err)}), 404
