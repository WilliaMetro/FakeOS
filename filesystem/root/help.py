import os

def app(args):
    print("Available commands:")
    for file in os.listdir():
        if file.endswith(".py") and file != "launchup.py":
            print(" -", file.replace(".py", ""))
