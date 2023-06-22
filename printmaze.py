def printmaze(maze,spaces_good):
    for j in range(len(maze[0])):
        line1 = ''
        line2 = '   '
        for i in range(len(maze[1])):
            if [i,j] in spaces_good:
                line1 = line1 + 'o '
            else:
                line1 = line1 + '  '
            if maze[i,j] % 4 == 2 or maze[i,j] % 4 == 3:
                line1 = line1 + '| '
            else:
                line1 = line1 + '  '
            if i != 0:
                if maze[i,j] % 2 == 1:
                    line2 = line2 + '--- '
                else:
                    line2 = line2 + '    '
        print(line1)
        print(line2)