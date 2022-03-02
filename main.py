import os
import sys

# Takes values from main()and attaches them to output values in action.yml
def set_action_output(name: str, value: str):
    sys.stdout.write(f'::set-output name={name}::{value}\n')


def main():
    # Obtain input variables
    path = os.environ["INPUT_PATH"]
    extension = os.environ["INPUT_TYPE"]
    input = os.environ["INPUT_FILEINPUT"]
    accessfile = os.environ["INPUT_FILE"]
    extadd = os.environ["INPUT_EXTCHANGE"]
    ext = os.environ["INPUT_EXT"]

    paths = []
    names = []
    extaddpaths = []
    inputfiles = accessfile.split(',')

    # Run through input to find files with desired extension
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

    # Run through files to add changed extension (useful for file converting actions)
    if extadd == "true":
        for file in inputfiles:
            if file.endswith(f'{extension}'):
                extaddpaths.append(os.path.splitext(file)[0]+ext)

    set_action_output('paths', paths)
    set_action_output('names', names)
    set_action_output('extaddpaths', extaddpaths)

    sys.exit(0)


if __name__ == "__main__":
    main()