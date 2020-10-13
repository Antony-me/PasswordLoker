import unittest # Importing the unittest module
from user import User # Importing the contact class

class TestContact(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Tolly", "0000") #create a new user

    # def tearDown(self):
    #         '''
    #         tearDown method that does clean up after each test case has run.
    #         '''
    #         user_list = [] #Return the list to defautl

    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.user,"Tolly")
        self.assertEqual(self.new_password.user,"0000")



if __name__ == '__main__':
    unittest.main()