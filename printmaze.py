def printmaze(maze,x,y):
    for j in range(x):
        line1 = ''
        line2 = '   '
        for i in range(y):
            k = maze[(str(i),str(j))]
            if k[2] == 'empty':
                line1 = line1 + 'o '
            else:
                line1 = line1 + '  '
            if k[0] == 1:
                line1 = line1 + '| '
            else:
                line1 = line1 + '  '
            if i != 0:
                if k[1]:
                    line2 = line2 + '--- '
                else:
                    line2 = line2 + '    '
        print(line1)
        print(line2)