import os
import sys

def getfiles(path):
    fs = []

    items = os.listdir(path)

    for item in items:
        if os.path.isfile(item):
            fs.append(item)

    return fs

def getdirectories(path):
    ds = []

    items = os.listdir(path)

    for item in items:
        if not os.path.isfile(item):
            ds.append(item)

    return ds

if __name__ == "__main__":
    opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]

    cwd = os.getcwd()

    files = []
    directories = []
    out = []
    
    if '-d' in opts:
        directories = getdirectories(cwd)
    
    files = getfiles(cwd)

    for f in files:
        out.append(f)
    
    for d in directories:
        out.append(d)

    out.sort()

    for item in out:
        print(item)
    