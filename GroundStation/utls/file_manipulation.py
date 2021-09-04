import os


def create_file(file):
    try:
        f = open(file, "x")
        return file
    except:
        raise FileExistsError

def write_file(file, info):
    # append to existing file
    f = open(file, "a")
    f.write(f'{info}\n')
    f.close()

def read_file(file):
    # open file in read mode
    f = open(file, "r")
    info = f.read()
    f.close
    return info

def check_file(file):
    return os.path.exists(file)