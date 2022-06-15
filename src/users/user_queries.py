from database_session import DatabaseSession
from models import User
class UserQueries():
    def add_user(user):
        session = DatabaseSession()

        try:
            session.add(user)
            session.commit()
            return True, ""
        except Exception as e:
            session.rollback()
            if "username" in str(e.__cause__):
                return False, "username already exists, please change."
            if "email" in str(e.__cause__):
                return False, "email already exists, please change."
            return False, "error creating user, please try again."

    def get_user(token):
        session = DatabaseSession()
        return session.query(User).filter_by(token=token).first()