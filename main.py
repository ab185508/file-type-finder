import os
import sys


def set_action_output(name: str, value: str):
    sys.stdout.write(f'::set-output name={name}::{value}\n')


def main():
    path = os.environ["INPUT_PATH"]
    print(path)
    extension = os.environ["INPUT_TYPE"]
    print(extension)
    input = os.environ["INPUT_FILEINPUT"]
    print(input)
    accessfile = os.environ["INPUT_FILE"]
    print(accessfile)

    paths = []
    names = []
    inputfiles = accessfile.split(',')
    
    if input == "true":
        for file in inputfiles:
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