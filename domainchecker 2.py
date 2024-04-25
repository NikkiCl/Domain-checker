domainwhitelist = list()
is_admin = False
import mmap

def load_domain_file():
    global domainwhitelist
    try:
        with open('list.txt', 'r') as file:
         for line in file:
            domainwhitelist.append(line.strip())
    except FileNotFoundError:
        pass
#Opens the txt file, if there is not one, it nulls it. 

def getDomainFromEmail(email):
    added = email.split('@')[-1]
    return added
# splits the string from the '@' symbol, and the -1 means it'll check the latter half of the domain. i.e gmail.com
def checkDomain(emailtoCheck):
    global domainwhitelist
    domainToCheck = getDomainFromEmail(emailtoCheck)
    if domainToCheck.lower() in domainwhitelist:
        print(f"{emailtoCheck} is APPROVED")
        return True
    else:
        print(f"WARNING! {emailtoCheck} is unknown")
        return False
#checks whether the email entered is in the domain whitelist

def checkEmail():
    emailToCheck = input('Please enter your email ')
    checkDomain(emailToCheck)
#Utilises the functions above in order to check whether the email is approved


def checkFileEmail():
    filename = input("Enter a file ")
    try:   
        with open(filename, 'r') as file:
            for line in file:
                checkDomain(line.strip())
    except FileNotFoundError:
        print("File not found")
#when user enters a file name it simultaneously email checks every single string in that file.  


def loginadmin():
    global is_admin
    password = input('Enter the admin password ')
    if password == 'POORSEC':
    # I understand that using hardcode passwords in your code could be a vulnerability, but since this is a small project I'm not gonna fix it.
        is_admin = True
    else:
        print('Sorry! This password is incorrect')
    return
# Asks user for a password, if its not POORSEC, the user is not granted admin
def logoutadmin():
    global is_admin
    is_admin = False
    return

def add_approved_domain():
    global is_admin
    global domainwhitelist
    if is_admin is False:
        print('You must be logged in as an admin')
        return
    added = input("Enter a new domain ")
    added = added.lower()

    if added in domainwhitelist:
        return
    domainwhitelist.append(added)
    with open('list.txt','a') as file:
        file.write(added + '\n')
    return 
   # It opens the txt file and adds the user input onto the text file.
   # Sometimes there is a bug where when you first add something onto approved domain it'll clash with the previous added txt.
   # Not really sure how to fix this since \n should be adding a new line, but it seems to be only for the first attempt at adding a new domain.     
def quit():
    print("Thank you for using our application")
    exit()
    #I know that exit should be replaced with sys.exit but it works either way since this is a small project

def get_menu_input():
    selection = input('Enter a valid menu option ')
    return selection

def navigate(selection):
    if selection == '1':
        checkEmail()
    elif selection == '2':
        checkFileEmail()
    elif selection == '3' and is_admin is False:
        loginadmin()
    elif selection == '3' and is_admin is True:
        logoutadmin()
    elif selection == '4' and is_admin is True:
        add_approved_domain()
    elif selection == '5':
        quit()
    else:
        print("Uknown selection")

def main():
    global is_admin
    load_domain_file()
    while True:
        print("Welcome to domain checker!")
        print('--------------------------')
        print("1. Check an email address")
        print("2. check the file of an email address")
        if is_admin is False:
            print('3. Log in as admin')
        else:
            print('3 Log out of admin')
            print('4. Add an approved domain')
        print('5. Quit the program.')
        print()
        selection = get_menu_input()
        navigate(selection)
# Presents the menu and option 4 wont show unless you are an admin
main()
            



    