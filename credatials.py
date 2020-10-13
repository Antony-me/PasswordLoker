from user import User

class Credential(User):
    '''
    list of saved passwords
    '''

    saved_passwords_list = []


    def __init__(self, social_media, password):
        self.social_media = social_media
        self.password = password


    '''
    Class method to save the user_credatials to the save_password_list
    '''

    @classmethod
    def save_password(self):

        password.saved_passwords_list .append(self)

        
