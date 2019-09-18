def removeComments(line):
    i = line.find('#')
    if i >= 0:
        line = line[:i]

    return line.strip()

def parsePkgList(file):
    pkgs = []

    with open(file) as f:
        for line in f.readlines():
            line = removeComments(line)
            line = line.strip()
            if line != "":
                pkgs.append(line)

    return pkgs
