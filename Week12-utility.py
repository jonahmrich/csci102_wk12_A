def PrintOutput(string):
    print('OUTPUT', string)

def LoadFile(filename):
    with open(filename, 'r') as f:
        contents = f.readlines()
    PrintOutput(contents)
