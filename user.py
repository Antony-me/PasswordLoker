class User:
    '''
    List of registered  users
    '''
    
    user_list = []

   
    def __init__(self, user, password):
        self.user = user
        self.password = password

    '''
    Class method to save the user to the user_list
    '''

    @classmethod
    def save_user(self):
        self.user_list.append(self)




# if __name__ =='__main__':
#     main()










            

           

      
