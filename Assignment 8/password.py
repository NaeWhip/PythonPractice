# main function of password validation
def valid_pass(use_password):

    # invalidated password errors
    pass_errors = []

    # Lets the user know that the password is too short
    if len(use_password) < 8:
        pass_errors.append("- " + "Password must be at least 8 characters long.")

    # Lets the user know that the password must meet the requirements for validations
    if any(char.isspace() for char in use_password) or not any(char.isdigit() for char in use_password) or not any(char.isupper() for char in use_password):
        pass_errors.append("- " + "Password must contain at least one uppercase letter, one lowercase letter, and one digit.")

    # Lets the user know that there should be no spaces in the password
    space_character = " "
    if any(char in space_character for char in use_password):
        pass_errors.append("- " + "Password must contain no spaces.")

    # Lets the user know that there should be no special character in the password
    special_character = "$%#^@$!*"
    if any(char in special_character for char in use_password):
        pass_errors.append("- " + "Password must contain no symbols.")

    # returns the invalidated password errors
    return pass_errors


def main():

     
    while True:
        # prompts the user and checks for password errors
        user_password_input = input("Enter a password: ")

        validation_error = valid_pass(user_password_input)

        # Lets the user know that their password was valid
        if not validation_error:
            print("Password is valid.")
            break

        # Finds an invalidation and prompts the user of the password error
        else:
            for pass_error in validation_error:
                print(pass_error)

        print("Password is invalid.")


# Call the main function
if __name__ == "__main__":
    main()