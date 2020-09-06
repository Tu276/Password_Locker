import unittest
from locker import User
from locker import Credentials

class TestUser(unittest.TestCase):
    '''
    test class that defines test cases for the User class behaviours


    Args:
    
     unittest.TestCase: TestCase class that helps in creating test cases

    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        
        self.new_user = User("tu276","nathan") #create user object

    def test_init(self):
         
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.login_username,"tu276")
        self.assertEqual(self.new_user.user_password,"nathan")

if __name__ == '__main__':
    unittest.main()

class TestCredentials(unittest.TestCase):
    '''
    test class that defines test cases for the Credentials class behaviours


    Args:
    
     unittest.TestCase: TestCase class that helps in creating test cases

    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_crendentials = Credentials("facebook","tu276","nathan") # create credentials object
        '''
        test_init test case to test if the object is initialized properly
        '''
        
        self.assertEqual(self.new_crendentials.account_name,"facebook")
        self.assertEqual(self.new_crendentials.account_username,"tu276")
        self.assertEqual(self.new_crendentials.account_password,"nathan")



if __name__ == '__main__':
    unittest.main()