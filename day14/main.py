

def star1():
    rules = dict()
    polymer = ""
    with open('input.in', 'r') as file:
        polymer = file.readline().strip('\n')
        for line in file:
            if line == '\n':
                continue
            tmp = line.strip('\n').split(' ')
            rules[tmp[0]] = tmp[2]
    
    elems = dict()
    for el in polymer:
        try:
            elems[el] += 1
        except:
            elems[el] = 1
    

    for i in range(10):
        l = 2 * len(polymer) - 2
        for j in range(0, l, 2):
            hd = polymer[:j+1]
            tl = polymer[j+1:]
            curr = polymer[j:j+2]
            polymer = hd + rules[curr] + tl
            try:
                elems[rules[curr]] += 1
            except:
                elems[rules[curr]] = 1


    max_ = -1
    min_ = 20000000000000
    for el in elems:
        if elems[el] > max_:
            max_ = elems[el]
        if elems[el] < min_:
            min_ = elems[el]
    
    print("the difference is %d\n" % (max_ - min_))


def star2():
    rules = dict()
    pairs = dict()
    polymer = ""
    with open('input.in', 'r') as file:
        polymer = file.readline().strip('\n')
        for line in file:
            if line == '\n':
                continue
            tmp = line.strip('\n').split(' ')
            rules[tmp[0]] = tmp[2]

    for i in range(1, len(polymer)):
        try:
            pairs[polymer[i-1:i+1]] += 1
        except:
            pairs[polymer[i-1:i+1]] = 1


    elems = dict()
    for el in polymer:
        try:
            elems[el] += 1
        except:
            elems[el] = 1

    # everything fine until here

    for i in range(40):
        tmp = pairs.copy()
        for k in pairs:
            if pairs[k] == 0:
                continue
            tmp[k] -= pairs[k]
            fst = k[0]
            trd = k[1]
            snd = rules[k]
            try:
                elems[snd] += pairs[k]
            except:
                elems[snd] = pairs[k]
            try:
                tmp[fst+snd] += pairs[k]
            except:
                tmp[fst+snd] = pairs[k]
            try:
                tmp[snd+trd] += pairs[k]
            except:
                tmp[snd+trd] = pairs[k]
        pairs = tmp
   
    
    max_ = -1
    min_ = 20000000000000000
    for el in elems:
        if elems[el] > max_:
            max_ = elems[el]
        if elems[el] < min_:
            min_ = elems[el]

    print("the difference for the second star is %d\n" % (max_ - min_))

star1()
star2()
