def app(program_args):
    import shelve, hashlib

    username = input("New username: ")
    password = input("New password: ")

    if username == '':
        print("Username cannot be empty")
        return

    password_hash = hashlib.sha256(password.encode()).hexdigest()

    db = shelve.open("/mnt/wwn-0x5000039366d00945-part1/Media/bat project/FakeOS/filesystem/data/system/main")

    users = db["users"]

    # kiểm tra trùng
    for user in users:
        if username in user:
            print("User already exists")
            db.close()
            return

    users.append({username: password_hash})
    db["users"] = users

    db.close()
    print("User created successfully")