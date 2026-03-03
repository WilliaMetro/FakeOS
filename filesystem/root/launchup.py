class RuntimeError(BaseException):
    pass


def launchup(*program_args):
    if not program_args:
        print("No command entered.")
        return

    command = program_args[0]

    try:
        module = __import__(command)

        if hasattr(module, "app"):
            module.app(program_args)
        else:
            print(f"Command '{command}' exists but has no app() function.")

    except ModuleNotFoundError:
        print(f"Command '{command}' not found.")

    except Exception as e:
        print("Runtime error:", e)