def app(program_args):
    import hashlib, shelve, os

    username = input("Username: ")
    password = input("Password: ")

    if username == '' or password == '':
        print("Username or password error, try again")
        return None

    passwordCheck = hashlib.sha256(password.encode('utf-8')).hexdigest()

    base_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.abspath(os.path.join(base_dir, "../../filesystem/data/system/main"))

    userdb = shelve.open(path)

    realPassword = None

    for user in userdb["users"]:
        if username in user:
            realPassword = user[username]
            break

    userdb.close()

    if realPassword and realPassword == passwordCheck:
        return username
    else:
        print("Username or password error, try again")
        return None
