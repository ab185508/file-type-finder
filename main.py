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
    extadd = os.environ["INPUT_EXTCHANGE"]
    print(extadd)
    ext = os.environ["INPUT_EXT"]
    print(ext)

    paths = []
    names = []
    extpaths = []
    inputfiles = accessfile.split(',')

    if input == "true":
        for file in inputfiles:
            if file.endswith(f'{extension}'):
                paths.append(file)
                splitpath = file.split('/')
                filename = splitpath[len(splitpath)-1]
                names.append(os.path.splitext(filename)[0])
    else:
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(f'{extension}'):
                    path_str = root + '/' + str(file) + ' '
                    paths.append(path_str)
                    names.append(os.path.splitext(file)[0])

    if extadd == "true":
        for file in inputfiles:
            if file.endswith(f'{extension}'):
                extpaths.append(os.path.splitext(file[0])+ext)

    set_action_output('paths', paths)
    set_action_output('names', names)
    set_action_output('extaddpaths', extpaths)
    print(paths)

    sys.exit(0)


if __name__ == "__main__":
    main()