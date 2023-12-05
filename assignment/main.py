from funcsi import register, login

k = int(input('Ruyxatdan utish/Royxatdan utilgan(0/1): '))
is_registered = False

if k == 0:
    is_registered = register()


else:
    users_id = login()
    print(users_id)
