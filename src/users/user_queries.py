from crud_interfaces import CreateObjectInterface, ReadObjectInterface
from database_session import DatabaseSession
from models import User

# This class applies the Single Responsibility Principle (SRP)
# Its only objective is to query the User model
class UserQueries(CreateObjectInterface, ReadObjectInterface):
    def create_one(user):
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

    def read_one(token):
        session = DatabaseSession()
        return session.query(User).filter_by(token=token).first()