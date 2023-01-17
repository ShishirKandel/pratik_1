
import json

def get_stored_username():
    file_name = "username.json"
    try:
        with open(file_name) as f_n:
            username = json.load(f_n)
    except FileNotFoundError:
        return None
    else:
        return username

# 
def get_new_username():
    username = input("what is your name? ")
    file_name = "username.json"
    with open(file_name, "w") as f_n:
        json.dump(username, f_n)
    return username

def greet_user():

    username = get_stored_username()
    if username:
        correct = input("Are you " + username + "? (y/n) ")
        if correct == "y":
            print("welcome " + username)
        else:
            username = get_new_username()
            print("come back soon " + username)
    else:
        username = get_new_username()
        print("come back soon " + username)

greet_user()