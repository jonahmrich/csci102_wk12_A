def PrintOutput(string):
    print('OUTPUT', string)

def LoadFile(filename):
    with open(filename, 'r') as f:
        contents = f.readlines()
    PrintOutput(contents)

def UpdateString(str1, str2, index):
    str1a = str1[:index] + str2
    str1b = str1[index + 1:]
    str1 = str1a + str1b
    PrintOutput(str1)
    
