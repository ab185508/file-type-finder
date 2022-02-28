import os
import sys


def set_action_output(name: str, value: str):
    sys.stdout.write(f'::set-output name={name}::{value}\n')


def main():
    path = os.environ["INPUT_PATH"]
    extension = os.environ["INPUT_TYPE"]
    
    paths = ''
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(f'{extension}'):
                paths = paths + root + '/' + str(file) + ' '
                names = os.path.splitext(file)[0]

    set_action_output('paths', paths)
    set_action_output('names', names)
    print(paths)

    sys.exit(0)


if __name__ == "__main__":
    main()