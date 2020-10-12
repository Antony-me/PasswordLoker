class User:

    user_list = []

    def save_user(self):

        user.user_list.append(self)

    def __init__(self, user, password):
        self.user = user
        self.password = password

# new_user = User("created_user", "created_password")

class Credential(User):

    saved_passwords_list = []

    def save_password(self):

        password.saved_passwords_list .append(self)

    def __init__(self, social_media, password):
        self.social_media = social_media
        self.password = password

        








            

           

      
