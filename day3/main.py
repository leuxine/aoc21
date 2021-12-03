
def star1():
    with open('input.in', 'r') as file:
        count = []
        for line in file:
            if len(count) == 0:
                for i in range(len(line)):
                    try:
                        n = int(line[i])
                        count.append([0, 0])
                    except:
                        pass

            for i in range(len(line)):
                try:
                    n = int(line[i])
                    # save them in little endian
                    count[-(i+1)][n] += 1
                except:
                    pass

        gamma = 0
        epsilon = 0
        two = 1 

        for bit in count:
            g = bit.index(max(bit))
            e = 1 - g 
        
            gamma += g * two
            epsilon += e * two
            two *= 2

        print("gamma=%d, epsilon=%d, power=%d\n" % (gamma, epsilon, gamma * epsilon))

def star2():
    lines = []
    with open('input.in', 'r') as file:
        for line in file:
            lines.append(line.strip('\n'))
    
    bit = 0
    ox = lines[:]
    co = lines[:]
    while(len(ox) > 1 or len(co) > 1):
        most_ox = [0, 0]
        for o in ox:
            try:
                most_ox[int(o[bit])] += 1
            except:
                pass

        max_ox = 0 if most_ox[0] > most_ox[1] else 1


        for o in list(ox):
            try:
                if int(o[bit]) != max_ox:
                    ox.remove(o)
            except: 
                ox.remove(o)

        least_co = [0, 0]
        for c in co:
            try:
                least_co[int(c[bit])] += 1
            except:
                pass

        min_co = 1 if least_co[1] < least_co[0] else 0 
      
        for c in list(co):
            if len(co) == 1:
                break
            try:
                if int(c[bit]) != min_co:
                    co.remove(c)
            except:
                co.remove(c)

        bit += 1

    print(ox[0])
    print(co[0])

    two = 2**(len(ox[0])-1)
    ox_rating = 0
    for o in ox[0]:
        try:
            ox_rating += int(o) * two
            two /= 2 
        except:
            pass

    two = 2**(len(co[0])-1)
    co_rating = 0
    for c in co[0]:
        try:
            co_rating += int(c) * two
            two /= 2
        except:
            pass
    
    print("oxigen rating = %d, co2 rating = %d, life support rating = %d\n" %
            (ox_rating, co_rating, ox_rating * co_rating))

star1()
star2()
