from database_session import DatabaseSession

class UserQueries():
    def add_user(user):
        session = DatabaseSession()

        try:
            session.add(user)
            session.commit()
            return True
        except Exception as e:
            return False
