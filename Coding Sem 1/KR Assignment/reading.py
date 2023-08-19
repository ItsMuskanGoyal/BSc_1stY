def main():
    print('WAY 1 :\n')
    file = open('oldfile.txt', 'r')
    print(file.read())
    file.close()
    print()


    print('WAY 2 :\n')
    file = open('oldfile.txt', 'r')
    print(file.readlines())
    file.close()
    print()

    print('WAY 3 :\n')
    file = open('oldfile.txt', 'r')
    line = file.readline() 
    while line != '':
        print(line, end='')
        line = file.readline()
    print()
    file.close()

    print('WAY 4 :\n')
    file = open('oldfile.txt', 'r')
    for line in file:
        print(line, end='')
    print('\n\n')
    file.close()


main()