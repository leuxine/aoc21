

def stars():
    dots = set()
    xtoy = dict()
    with open('input.in', 'r') as file:
        for line in file:
            if line == "\n":
                break
            coord = line.strip('\n').split(',')
            dots.add(tuple((int(coord[0]), int(coord[1]))))
            
        for fold in file:
            f = fold.split(' ')[2]
            xy = f.split('=')[0]
            num = int(f.strip('\n').split('=')[1])

            tmp = set()
            for dot in dots:
                if xy == 'x':
                    if dot[0] > num:
                        diff = dot[0] - num
                        tmp.add(tuple((num - diff, dot[1])))
                    else: 
                        tmp.add(dot)
                else:
                    if dot[1] > num:
                        diff = dot[1] - num
                        tmp.add(tuple((dot[0], num - diff)))
                    else:
                        tmp.add(dot)

            print("there are %d dots after one fold\n" % (len(tmp)))
            dots = tmp
        
        grid = [['.' for j in range(50)] for i in range(50)]

        for dot in dots:
            grid[dot[0]][dot[1]] = '#'

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                print(grid[i][j], "", end="")
            print()

stars()
