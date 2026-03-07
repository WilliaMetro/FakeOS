def app(program_args):
    import shelve
    import hashlib
    import os

    username = input("New username: ")
    password = input("New password: ")

    if username == "":
        print("Username cannot be empty")
        return

    password_hash = hashlib.sha256(password.encode()).hexdigest()

    base_dir = os.path.dirname(os.path.abspath(__file__))

    path = os.path.abspath(os.path.join(base_dir, "../../filesystem/data/system/main"))

    db = shelve.open(path)

    users = db.get("users", [])

    for user in users:
        if username in user:
            print("User already exists")
            db.close()
            return

    users.append({username: password_hash})
    db["users"] = users

    db.close()

    print("User created successfully")