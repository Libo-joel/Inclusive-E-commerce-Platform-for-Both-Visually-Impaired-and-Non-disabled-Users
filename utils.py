import json

def load_users():
    try:
        with open('users.json', 'r') as file:
            users = json.load(file)
    except FileNotFoundError:
        users = []
    return users


def save_users(users):
    with open('users.json', 'w') as file:
        json.dump(users, file, indent=4)


    


