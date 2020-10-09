def main():

    while True:
        print("Hi and welcome to your password vault")
        print("-" * 100)
        print("Select a code to continue with: \n \nNU--for creating new User:\nLG-- to Login as an existing User: \nEX-- to exit \n")
        print("-" * 100)

        short_code = input().upper()
        print("-" * 100)

        if short_code =='NU':
            print("Enter Username of your choice")
            created_new_user = input()

            print("Create a password")
            created_new_password = input()

            print("Confirm Entered password")
            confirm_password = input()

            while confirm_password != created_new_password:
                print("Password did not match. Please make sure paswwords match")
                print("Please Re- Enter your Password")
                created_new_password = input()


            else:
                print(f"Congratulations  {created_new_user} Your account is ready")
                print("-" * 100)

                print("Login to your account")
                print("Enter Username")
                entered_username = input()

                print("Enter Your Password")
                entered_password = input()
            while entered_username != created_new_user or entered_password != created_new_password:
                print("Invalid username or password")
                print("Please Enter Valid Username and Paswword")

                print("Enter Username")
                entered_username = input()
                print("Enter Your Password")
                entered_password = input()
            else:
                print(f"Congratulations {entered_username} welcome to your vault")
                print("-" * 100)

        elif  short_code == 'LG':
            print("Welcome to Your Vault ")
            print("Enter your username")
            default_user_name = input()

            print("Please enter Your Password")
            default_user_password = input()
            print("-" * 100)
            while default_user_password != "defaultUser" or default_password != default_user_password:
                print("Invalid username or Password")
                print("If you want to login as a default user enter: Username-defaultUser and password-  00000")

                print("Enter Default Username")
                default_user_name = input()

                print("Enter deault password")
                default_password = input()
            else:
                print("You have succesfully Logged into your account")
                print("-" * 600)
                print("-" * 20)
        elif short_code == "EX":
            break
        else:
            print("Enter a valide short code to proceed.")


if __name__ =='__main__':
    main()





            










    


