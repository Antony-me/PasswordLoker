from user import User
import string
import secrets

def main():

    while True:
        print("Hi and welcome to your Password Vault")
        print("Please select a code to continue with:")
        print("=" * 70)
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
            

            while confirm_password != created_new_password:
                print("Password did not match. Please make sure paswwords match")
                print("Please Re- Enter your Password:")
                created_new_password = input()
                
            else:

                print("*" * 70)
                print(f"*********** Congratulations  {created_new_user.upper()},  Your account is ready *************")
                print("*" * 70)

        elif  short_code == 'LG':
            print("Welcome to Your Vault: ")
            print("Enter your username:")
            entered_username = input()

            print("\nEnter Your Password:")
            entered_password = input()

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

                        alphabet = string.ascii_letters + string.digits
                        password = ''.join(secrets.choice(alphabet) for i in range(8))

                        f= open("Passwords/passwords.txt","w")
                        f.write("Your Twitter username is:")
                        f.write(username )
                        f.write("\nYour Twitter Password is:")
                        f.write(password )

                        f.close()
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

                        alphabet = string.ascii_letters + string.digits
                        password = ''.join(secrets.choice(alphabet) for i in range(8))

                        f= open("Passwords/ig.txt","w")
                        f.write("Your Instagram username is:")
                        f.write(username )
                        f.write("\nYour Instagram Password is:")
                        f.write(password )

                        f.close()

                    elif selection == "E":

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





            









    


