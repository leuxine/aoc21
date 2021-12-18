
def stars(star):
    with open('input.in', 'r') as file:
        grid = []
        for line in file:
            if line == '\n':
                break

            tmp = []
            for c in line.strip('\n'):
                tmp.append(int(c))

            grid.append(tmp)

    rows = len(grid)
    cols = len(grid[0])

    flashes = 0
    
    stop = 0

    while True:
       
        print("iteration %d:\n" % (stop+1))

        changed = [[False for j  in range(cols)] for i in range(rows)]
        first = True

        while True:
            changes = 0
            for i in range(rows):
                for j in range(cols):
                    if first:
                        grid[i][j] += 1
                    if grid[i][j] > 9 and not changed[i][j]: 
                        
                        changes += 1
                        changed[i][j] = True
                        
                        for i_ in range(i-1, i+2):
                            for j_ in range(j-1, j+2):
                                if (i_ == i and j_ == j) or i_ < 0 or i_ >= rows \
                                or j_ < 0 or j_ >= cols:
                                    continue

                                grid[i_][j_] += 1
                    

            first = False
            if changes == 0:
                break

        all_zero = True
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] > 9:
                    flashes += 1
                    grid[i][j] = 0
                if grid[i][j] != 0:
                    all_zero = False
                print(grid[i][j], "", end="")
            print()

        print("the number of flashes was %d\n" % (flashes))

        if (stop == 99 and star == 1) or (all_zero and star == 2):
            break
        
        stop += 1

stars(1)
stars(2)
