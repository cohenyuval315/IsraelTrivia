from flask_security import UserMixin, RoleMixin


class User(UserMixin):
    """

    """
    def __init__(self, password_token, username, password):
        self.password_token = password_token
        self.username = username
        self.password = password
        self.role = ["user"]


class Role(RoleMixin):
    """

    """
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.role = ["user", "admin"]

