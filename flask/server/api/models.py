from flask_security import UserMixin, RoleMixin


class User(UserMixin):
    """

    """
    def __init__(self, id, username, password):
        self.id = id
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

