
def make_fish():
    fish = []

    with open('input.in', 'r') as file:
        fish = file.readline().strip('\n').split(',')

    for i in range(len(fish)):
        fish[i] = int(fish[i])

    return fish

# old brute force approach
def star1():

    fish = make_fish()

    for i in range(80):
        tmp = []
        for f in fish:
            if f == 0:
                tmp.append(6)
                tmp.append(8)
            else:
                tmp.append(f-1)
        fish = tmp

    print("number of fish at the end: %d\n" % (len(fish)))


def star(days):
    fish = make_fish()

    amount = [0] * 10

    for f in fish:
        amount[f] += 1
   
    for i in range(days):
        for j in range(len(amount)-1):
            if j == 0:
                amount[9] = amount[j]
                amount[7] += amount[j]
            amount[j] = amount[j+1]
        
        amount[9] = 0
            
    count = 0
    for a in amount:
        count += a
    
    print("the number of fish at the end of %d days is %d\n" % (days, count))

star(80);
star(256);
