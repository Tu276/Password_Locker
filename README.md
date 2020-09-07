# Password Locker

#### An amazing application that will help us manage our passwords and even generate new passwords for us.

# Kirimi Nathan

## Description
Password Locker is a terminal run app that allows users to store credentials usernames and passwords of their various accounts.


## User Stories

As a user I would like:
* To create an account with my details - log in and password
* Store my existing login credentials

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display codes for navigation | **in terminal $./run.py** | Welcome choose an option.. |
| Display prompt for creating an account | **cu** | Enter your username|
| Display prompt for login in | **li** | Enter your luname  i.e login username|
| Display codes for navigation | **successful login** | Choose an option: cc - Create Credential, dc - Display Credentials, copy - Copy Credential, ex - exit |
| Display prompt for creating a credential | **cc** |  your username and password |
| Display a list of credentials | **dc** | list of saved credentials |
| Display prompt for which credential to copy | **copy** | details of the copied credential saved to clipboard |
| Exit application | **ex** | Exit the current navigation stage |
| Display codes for navigation | **In terminal: $./run.py** | Welcome, choose an option... |
| Display prompt for creating an account | **Enter: ca** | Enter your login_username |
| Display prompt for login in | **Enter: li** | Enter your account name and password |
| Display codes for navigation | **Successful login** | Choose an option..... |
| Display prompt for creating a credential | **Enter: cc** | Enter your username and password |
| Display a list of credentials | **Enter: dc** | Prints a list of saved credentials |
| Display prompt for which credential to copy | **Enter: copy** | Enter credential you wish to copy. |
| Exit application | **Enter: ex** | Exit the current navigation stage |

## SetUp / Installation Requirements
### Prerequisites
what you need:
    * python3.8
    * $ chmod +x Password_Locker.py
    * $ ./run.py

## Testing the Application
* To run the tests for the class file:

        $ python3.8 locker_test.py

## Technologies Used
* Python3.8
