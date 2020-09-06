import pyperclip


class User:
    """
    class that generates new users
    """

    user_List = []


    def __init__(self,login_username,user_password):


        self.login_username  = login_username
        self.user_password = user_password

    def save_user(self): #method saves user object into user_list
        
        User.user_List.append(self)

    def delete_user(self): 
        '''
        method deletes users
        '''

        User.user_List.remove(self)
           
        

class Credentials:
    """
    class that generates new credentials 
    """
    
    credentials_List = []


    def __init__ (self,account_name,account_username,account_password):

        self.account_name = account_name 
        self.account_username = account_username
        self.account_password = account_password


    def save_credentials(self):

        Credentials.credentials_List.append(self)

    def delete_credentials(self):
         
        Credentials.credentials_List.remove(self)

    @classmethod
    def find_by_account_name(cls,account_name):
        '''
        method takes account_name and returns  matching username
        '''
        for credentials in  cls.credentials_list:
            if credentials.account_name == account_name:
                return credentials

    @classmethod
    def credentials_exist(cls,account_name):
        '''
        methods checks if credentials exist
        
        returns:
        boolean depending whether the contact exists or not
        '''

        for credentials in cls.credentials_List:
            if credentials.account_name == account_name:
                return True

        return False


    @classmethod
    def display_credentials(cls):
        '''
        method that returns credentials
        '''

        return cls.credentials_List

    @classmethod 
    def copy_account_username(cls,account_name):
        credentials_found = Credentials.find_by_account_name(account_name)
        pyperclip.copy(credentials_found.account_username)

