class User:
    '''
    List of registered  users
    '''
    user_list = []

   
    def __init__(self, user, password):
        self.user = user
        self.password = password

    @classmethod
    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''
        User.user_list.remove(self)
    
    '''
    Class method to save the user to the user_list
    '''
    @classmethod
    def save_user(self):
        self.user_list.append(self)
        












            

           

      
