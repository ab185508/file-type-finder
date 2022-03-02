import os
import sys


def set_action_output(name: str, value: str):
    sys.stdout.write(f'::set-output name={name}::{value}\n')


def main():
    path = os.environ["INPUT_PATH"]
    extension = os.environ["INPUT_TYPE"]
    input = os.environ["INPUT_FILEINPUT"]
    accessfile = os.environ["INPUT_FILE"]

    paths = []
    names = []
    if input == "true":
        with open(accessfile, 'r') as f:
            data = f.read()
        for file in data:
            if file.endswith(f'{extension}'):
                path_str = root + '/' + str(file) + ' '
                paths.append(path_str)
                names.append(os.path.splitext(file)[0])
    else:
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(f'{extension}'):
                    path_str = root + '/' + str(file) + ' '
                    paths.append(path_str)
                    names.append(os.path.splitext(file)[0])

    set_action_output('paths', paths)
    set_action_output('names', names)
    print(paths)

    sys.exit(0)


if __name__ == "__main__":
    main()