def app(program_args):
    import shelve
    import os

    base_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.abspath(os.path.join(base_dir, "../../filesystem/data/system/main"))

    try:
        db = shelve.open(path)

        users = db.get("users", [])

        if len(users) == 0:
            print("No users found")
        else:
            print("User list:")
            for user in users:
                for name in user:
                    print(" -", name)

        db.close()

    except Exception as e:
        print("Error:", e)
