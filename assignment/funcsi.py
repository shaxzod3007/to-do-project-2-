from users import User, get_data


def register():
    first_name = input('Ismingizni kiriting: ')
    last_name = input('Sharifingizni kiriting: ')
    birth_date = input('Tugulgan sanangizni kiriting: ')
    email = input('emailingizni kiriting: ')
    username = input('Klichkangizni kiriting: ')
    password = input('Parolingizni kiriting: ')


    user = User(first_name, last_name,birth_date, email, username, password)
    user.append_to_json()

def login():
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    users = get_data()

    for user in users:
        if user['username'] == username and user['password'] == password:
            return user['id']
    return 0
