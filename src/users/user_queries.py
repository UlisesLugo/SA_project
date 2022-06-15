from database_session import DatabaseSession

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
                return False, "Username is duplicated, please change."
            if "email" in str(e.__cause__):
                return False, "Email already exists, please change."
            return False, "Error creating user, please try again."
