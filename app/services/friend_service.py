from app.models import Usuario, amigos
from app import db

class FriendService:

    @staticmethod
    def add_friend(current_user_id, friend_id):
        usuario1 = Usuario.query.get(current_user_id)
        usuario2 = Usuario.query.get(friend_id)

        if not usuario1 or not usuario2:
            raise ValueError("User not found")

        stmt = amigos.insert().values(usuario1_id=current_user_id, usuario2_id=friend_id)
        db.session.execute(stmt)
        db.session.commit()

        return {"message": "Friends added successfully"}


    @staticmethod
    def get_friends(current_user_id):
        current_user_id = int(current_user_id)
        result = db.session.query(amigos).filter(
            (amigos.c.usuario1_id == current_user_id) | (amigos.c.usuario2_id == current_user_id)
        ).all()
        friends = []
        for row in result:
            if row.usuario1_id == current_user_id:
                friend_id = row.usuario2_id
            else:
                friend_id = row.usuario1_id
            friend = Usuario.query.get(friend_id)
            if friend:
                friends.append(friend.to_dic())
        return friends



    @staticmethod
    def delete_friend(current_user_id, friend_id):
        current_user_id = int(current_user_id)
        friend_id = int(friend_id)

        deleted = db.session.query(amigos).filter(
            ((amigos.c.usuario1_id == current_user_id) & (amigos.c.usuario2_id == friend_id)) |
            ((amigos.c.usuario1_id == friend_id) & (amigos.c.usuario2_id == current_user_id))
        ).delete()

        if deleted == 0:
            raise ValueError("Friendship not found")

        db.session.commit()

        return {"message": "Friendship deleted successfully"}



