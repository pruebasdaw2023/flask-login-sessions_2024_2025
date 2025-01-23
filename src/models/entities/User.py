from werkzeug.security import check_password_hash, generate_password_hash

class User():

    def __init__(self, username, password, fullname=''):

        self.username = username
        self.password = password
        self.fullname = fullname

    @classmethod
    def check_password(cls, hashed_password, password):

        return check_password_hash(hashed_password, password)

# print(generate_password_hash('luis'))

