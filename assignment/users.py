import json

def get_data():
    try:
        with open('main.py', 'r') as f:
            users: list = json.load(f)
            return users
    except (FileNotFoundError, json.JSONDecodeError):
        with open('funcsi.py', 'w') as f:
            json.dump([], f, indent=4)
            return []

class User:

    def __init__(self, ism, sharif, tugulgan_sanasi, email, klichkasi, paroli):
        self.ism = ism
        self.sharif = sharif
        self.tugulgan_sanasi = tugulgan_sanasi
        self.email = email
        self.klichkasi = klichkasi
        self.__paroli = paroli

    def append_to_json(self):
        users = get_data()
        if not self.user_exists():
            user = {
                'id': users[-1]['id'] + 1 if len(users) != 0 else 1,
                'ism': self.ism,
                'sharif': self.sharif,
                'tugulgan_sanasi': self.tugulgan_sanasi,
                'email': self.email,
                'klichkasi': self.klichkasi,
                'paroli': self.__paroli
            }
            users.append(user)
            with open('users.json', 'w') as f:
                json.dump(users, f, indent=4)
            print('Mofaqiyatli qoshildi')
        else:
            print('Klichka yoki emaili mavjud')

    def user_exists(self):
        users: list = get_data()

        for user in users:
            if user['klichkasi'] == self.klichkasi or user['email'] == self.email:
                return True
        return False

