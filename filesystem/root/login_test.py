def app(program_args):
    import hashlib, shelve

    username = input("Username: ")
    password = input("Password: ")

    if username == '' or password == '':
        print("Username or password error, try again")
        return None

    passwordCheck = hashlib.sha256(password.encode('utf-8')).hexdigest()

    userdb = shelve.open("/mnt/wwn-0x5000039366d00945-part1/Media/bat project/FakeOS/filesystem/data/system/main")

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
    