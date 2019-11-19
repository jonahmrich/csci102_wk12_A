def PrintOutput(string):
    print('OUTPUT', string)

def LoadFile(filename):
    with open(filename, 'r') as f:
        contents = f.readlines()
    return contents

def UpdateString(str1, str2, index):
    str1a = str1[:index] + str2
    str1b = str1[index + 1:]
    str1 = str1a + str1b
    PrintOutput(str1)

def FindWordCount(file_list, word):
    file_str = ' '.join(file_list)
    count = file_str.count(word.lower()) + file_str.count(word.capitalize())
    return count

def ScoreFinder(names, scores, name):
    if name.lower() in names:
        PrintOutput('%s got a score of %d' %(name.capitalize(), scores[names.index(name.lower())]))
    elif name.capitalize() in names:
        PrintOutput('%s got a score of %d' %(name.capitalize(), scores[names.index(name.capitalize())]))
    else:
        PrintOutput('player not found')
