import re

def ReadFile(*files):
    '''
        Reads files from the specified path and prints its content
        This sofware should be executed on the same path where the files are located.
    '''
    output = open('output.txt', mode = 'w+', encoding = 'utf-8')
    
    for file in files:
        with open(file, encoding = 'utf-8') as openedFile:
            print("Occurrences in file:", openedFile.name)
            lineNumber = 0

            for line in openedFile:
                lineNumber += 1
                if TextMatchesPattern(line, 'hello'):
                    output.write(line) 
                    print('{:>4} {}'.format(lineNumber, line.rstrip()))

    output.close() 

def TextMatchesPattern(text, pattern):
    return bool(re.search(pattern, text))

if __name__ == '__main__':
    ReadFile('test.txt', 'test2.txt')