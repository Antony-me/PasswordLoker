from user import User
import string
import secrets

def main():
    ''' This is the start of the bot
    '''

    while True:
        print("Hi and welcome to your Password Vault")
        print("Please select a code to continue with:")
        print("=" * 70)
        ''' This is to help user to select what he wants to do
        '''

        print("\n \nNU--For Creating new User\nLG-- To Login as an existing User\nEX-- To exit \n")
        print("-" * 70)

        short_code = input().upper()
        print("-" * 70)

        if short_code =='NU':
            print("Enter Username of your choice:")
            created_new_user = input()

            print("Create a password:")
            created_new_password = input()

            print("Confirm Entered password:")
            confirm_password = input()

            '''
            This is to confirm the passwords match before proceeding
            '''
            
            while confirm_password != created_new_password:
                print("Password did not match. Please make sure paswwords match")
                print("Please Re- Enter your Password:")
                created_new_password = input()
                
            else:

                print("*" * 70)
                print(f"*********** Congratulations  {created_new_user.upper()},  Your account is ready *************")
                print("*" * 70)
            '''
            Log into your created account
            '''

        elif  short_code == 'LG':
            print("Welcome to Your Vault: ")
            print("Enter your username:")
            entered_username = input()

            print("\nEnter Your Password:")
            entered_password = input()

            '''
            Confirm the password  entered is same as the user entered when he opened account
            '''
            while entered_username != created_new_user or entered_password != created_new_password:
                print("Invalid username or password")
                print("Please Enter Valid Username and Paswword:")
            else:
                print("Select code to continue: \nTW: For Twitter \nIG: For Instagram \nPW: to view your saved passwords")
                short_code = input().upper()

                print("-" * 70)
                if short_code =='TW':

                    print(f"Select G for the system to generate password for you or select E to enter your own password:")
                    selection = input().upper()
                    if selection == 'G':
                        print("Enter your twitter Username")
                        username = input()
                        '''
                        If a user decides for the system to geneate password it is done using the imported modules string and secret a random password is generated
                        '''

                        alphabet = string.ascii_letters + string.digits
                        password = ''.join(secrets.choice(alphabet) for i in range(8))

                        '''
                        This is to write the saved password and username to a text file 
                        '''

                        f= open("Passwords/twitter.txt","w")
                        f.write("Your Twitter username is:")
                        f.write(username )
                        f.write("\nYour Twitter Password is:")
                        f.write(password )

                        f.close()

                        '''
                        This is if a user decides to  enter his/her own password
                        '''

                    elif selection == "E":

                        print("Enter your twitter Username")
                        saved_new_username = input()
                        print(f"Enter Your  Twitter Password:")
                        saved_new_password = input()

                        f= open("Passwords/twitter.txt","w")

                        f.write("Your Twitter username is:")
                        f.write(saved_new_username )
                        f.write("\nYour Twitter Password is:")
                        f.write(saved_new_password )

                        f.close()

                if short_code =='IG':

                    print(f'Select "G" for the system to generate a random password for you or select "E" to enter your own password:')
                    selection = input().upper()
                    if selection == 'G':
                        print("Enter your Instagram Username")
                        username = input()
                        '''
                        If a user decides for the system to geneate password it is done using the imported modules string and secret a random password
                        '''

                        alphabet = string.ascii_letters + string.digits
                        password = ''.join(secrets.choice(alphabet) for i in range(8))

                        f= open("Passwords/ig.txt","w")
                        f.write("Your Instagram username is:")
                        f.write(username )
                        f.write("\nYour Instagram Password is:")
                        f.write(password )

                        f.close()

                    elif selection == "E":

                        '''
                        This is if a user decides to  enter his/her own password
                        '''

                        print("Enter your Instagram Username")

                        saved_new_username = input()
                        print(f"Enter Your  Instagram Password:")
                        saved_new_password = input()

                        f= open("Passwords/ig.txt","w")

                        f.write("Your Instagram username is:")
                        f.write(saved_new_username )
                        f.write("\nYour Instagram Password is:")
                        f.write(saved_new_password )

                        f.close()


                if short_code =='PW':
                    '''
                    This is to open the text file that contains the usernames and passwords
                    '''
                    
                    f= open("Passwords/twitter.txt","r")
                    print(f.read())

                    print("\n")

                    f= open("Passwords/ig.txt","r")
                    print(f.read())

                    print("\n\n")

        elif short_code == "EX":
            break
        else:
            print("Enter a valide short code to proceed.")


if __name__ =='__main__':
    main()





            









    


