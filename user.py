class user:

    user_list = []


    def __init__(self, user, password):
        self.user = user
        self.password = password


        def save_user(self):

            user.user_list.append(self)


class credential(user):
    

    saved_passwords_list = []

    def __init__(self, social_media, password):
        self.social_media = social_media
        self.password = password

        def save_password(self):
            

            password.saved_passwords_list .append(self)





            

           

      
