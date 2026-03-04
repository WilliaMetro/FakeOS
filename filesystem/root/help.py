import os

def app(program_args):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    current_file = os.path.basename(__file__)

    py_files = [
        os.path.splitext(file)[0]
        for file in os.listdir(current_dir)
        if file.endswith(".py") and file != current_file
    ]

    for name in sorted(py_files):
        print(name)