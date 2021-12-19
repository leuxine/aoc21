

def star1():
    rules = dict()
    pairs = dict()
    polymer = ""
    with open('small.in', 'r') as file:
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
    
    for i in range(10):
        tmp = pairs.copy()
        for k in pairs:
            if pairs[k] == 0:
                continue
            tmp[k] -= 1
            fst = k[0]
            trd = k[1]
            snd = rules[k]
            try:
                tmp[fst+snd] += 1
            except:
                tmp[fst+snd] = 1
            try:
                tmp[snd+trd] += 1
            except:
                tmp[snd+trd] = 1
        pairs = tmp
        print(pairs)
        print()

    max_ = -1
    min_ = 9223372036854775807
    for k in pairs:
        if pairs[k] > max_:
            max_ = pairs[k]
        if pairs[k] < min_:
            min_ = pairs[k]

    print("the difference is %d\n" % (max_ - min_))

    

star1()
