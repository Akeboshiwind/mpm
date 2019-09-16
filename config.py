from configparser import ConfigParser

def removeComments(line):
    i = line.find('#')
    if i >= 0:
        line = line[:i]

    return line.strip()

def parseConfig(file):
    pkgs = []

    with open(file) as f:
        for line in f.readlines():
            line = removeComments(line)
            line = line.strip()
            if line != "":
                pkgs.append(line)

    return pkgs

def getAppConfig(path):
    return ConfigParser().read(path)
