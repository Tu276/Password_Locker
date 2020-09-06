class user:
    """
    class that generates new users
    """

    user_List = []


    def __init__(self,login_username,user_password):


        self.login_username  = login_username
        self.user_password = user_password


class credentials:
    """
    class that generates new credentials 
    """
    
    credentials_List = []


    def __init__ (self,account_name,account_username,account_password):

        self.account_name = account_name 
        self.account_username = account_username
        self.account_password = account_password