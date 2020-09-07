#!/usr/bin/env python3.8
from locker import User
from locker import Credentials


def create_user(luname,upassword):
    '''
    function create new user
    '''
    new_user = User(luname,upassword)

    return new_user

def save_users(user):
    '''
    save user function
    '''
    User.save_user


def verify_user(lunam,upassword):
	'''
	Function that verifies the existance of the user before creating credentials
	'''
	checking_user = User.user_exist(lunam,upassword)
	return checking_user


def create_credentials(accountName,accountUsername,accountPassword):
    '''
    function creates new credentials
    '''
    new_credentials = Credentials(accountName,accountUsername,accountPassword)

def save_credential(credentials):
    '''
    function to save credentials
    '''
    credentials.save_credentials()

def display_credentials():

    return Credentials.display_credentials()

def copys_account_name(account_name):
     
    return Credentials.copy_account_username(account_name)

def find_credentials(account_name):
    '''
    functions that finds credentials and returns the credentials
    '''
    return Credentials.find_by_account_name(account_name)

def check_existing_credentials(account_name):
    '''
    function that checks credentials exists
    '''
    return Credentials.credentials_exist(account_name)


def main():
    print("Hello Welcome to your credetials list. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
            print("Use these short codes : cn - create a new user, li - login, ex -exit the contact list ")

            short_code = input().lower()

            if short_code == 'cn':
                    print("New User")
                    print("-"*10)

                    print ("Enter username ....")
                    luname = input()

                    print("Enter password ...")
                    upassword = input()

                    save_users(create_user(luname,upassword)) # create and save new user
                    print ('\n')
                    print(f"user {luname} {upassword} created")
                    print ('\n')

            elif short_code == 'li':
                    print("-"*60)
                    print(' ')
                    print('To login, enter your account details:')
                    user_name = input('Enter your first name - ')
                    password = str(input('Enter your password - '))
                    user_exists = verify_user(luname,upassword)
                    if user_exists == user_name:

                

                    while True:
                            print("Use these short codes : cc - create a new credentials, dc - display credentials, fc -find a credential, exit -exit the creddentials list ")

                            short_code = input().lower()

                            if short_code == 'cc':
                                    print("New Credentials")
                                    print("-"*10)

                                    print ("Account name eg . twitter ....")
                                    accountName = input()

                                    print("username...")
                                    accountUsername = input()

                                    print("password ...")
                                    accountPassword= input()

                                    


                                    save_credential(create_credentials(accountName,accountUsername,accountPassword,)) # create and save new contact.
                                    print ('\n')
                                    print(f"New Credentials {accountName} {accountUsername} {accountPassword} created")
                                    print ('\n')

                            elif short_code == 'dc':

                                    if display_credentials():
                                            print("Here is a list of all your credentials")
                                            print('\n')

                                            for credentials in display_credentials():
                                                    print(f"{credentials.account_name} {credentials.account_username} .....{credentials.account_password}")

                                            print('\n')
                                    else:
                                            print('\n')
                                            print("You dont seem to have any credentials saved yet")
                                            print('\n')

                            elif short_code == 'fc':

                                    print("Enter the credential account name you want to search for")

                                    search_name= input()
                                    if check_existing_credentials(search_name):
                                            search_credentials = find_credentials(search_name)   
                                            print(f"{search_credentials.account_name} {search_credentials.account_username}")
                                            print('-' * 20)

                                            print(f"password.......{search_credentials.account_password}")
                                           
                                    else:
                                            print("That contact does not exist")

                            elif short_code == "exit":
                                    print("Bye .......")
                                    break
                            else:
                                    print("I really didn't get that. Please use the short codes")


                                    
            elif short_code == "ex":
                    print("Bye .......")
                    break
            else:
                    print("I really didn't get that. Please use the short codes")



if __name__ == '__main__':

    main()