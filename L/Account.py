class Account(dict):
    def __init__(self, name, password):
        self['username'] = name
        self['password'] = password

    def change_password(self, password):
        self['password'] = password