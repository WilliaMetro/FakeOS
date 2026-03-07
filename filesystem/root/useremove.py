def app(program_args):
    import shelve
    import os

    if len(program_args) < 2:
        print("Usage: useremove <username>")
        return

    target = program_args[1]

    base_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.abspath(os.path.join(base_dir, "../../filesystem/data/system/main"))

    db = shelve.open(path)

    users = db.get("users", [])

    new_users = []
    found = False

    for user in users:
        username = list(user.keys())[0]

        if username == target:
            found = True
        else:
            new_users.append(user)

    if found:
        db["users"] = new_users
        print("User removed:", target)
    else:
        print("User not found")

    db.close()