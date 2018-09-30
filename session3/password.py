while True:
    password_str = input("Enter the password: ")
    # if len(password_str) >= 8:
        # if password_str.isupper():
        #     print("The password must contain both upper and lower characters")
        # elif password_str.islower():
        #     print("The password must contain both upper and lower characters")
        # else:
        #     print("Ok")
        #     break

    if len(password_str) < 8:
        print("Not long enough")
    elif password_str.isdigit():
        print("Must not contain only digits")
    elif password_str.isupper():
        print("Must contain lowercase characters")
    elif password_str.islower():
        print("Must contain uppercase characters")
    else:
        print("Ok")
        break
    