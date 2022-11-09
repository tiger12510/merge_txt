import os,glob

def readfile(path: str):
    files_list = os.listdir(path)
    derict = {}
    for filename in glob.glob('*.txt'):
        with open(filename, 'r', encoding='utf-8') as file:
            derict[filename] = [x for x in file.read().splitlines() if x]

    with open('merge.txt', 'w', encoding='utf-8') as file:
        for key, value in sorted(derict.items(), key=lambda x: -len([x[1]])):
            file.write(key + '\n')
            file.write(str(len(value)) + '\n')
            file.write('\n'.join(value))
            file.write('\n')

readfile(os.getcwd())

