import os

def getfiles(path):
    fs = []

    items = os.listdir(path)

    for item in items:
        if os.path.isfile(item):
            fs.append(item)

    return fs

def run_app():
    files = []

    cwd = os.getcwd()

    files = getfiles(cwd)
    files.sort()

    for file in files:
        print(file)

if __name__ == "__main__":
    run_app()
