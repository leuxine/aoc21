

def stars():
    f = open('input.in', 'r')

    line = f.readline().replace(',', '').strip('\n').split(' ')

    tx = line[2].strip('x').strip('=').split('..')
    tx_0 = int(tx[0])
    tx_n = int(tx[1])

    ty = line[3].strip('y').strip('=').split('..')
    ty_0 = int(ty[0])
    ty_n = int(ty[1])

    print(tx_0)
    print(tx_n)
    print(ty_0)
    print(ty_n)
    
    s = abs(ty_0) 
      
    max_y = 0
    for i in range(s):
        max_y += i
  
    print("max y coordinate is %d" % max_y)
    

    tmp = tx_0
    min_ = 0
    for i in range(1, tx_0):
        if tmp < 0:
            min_ = i
            break
        tmp -= i

    tmp = tx_n
    max_ = 0
    for i in range(1, tx_n):
        if tmp < 0:
            break
        tmp -= i
        max_ = i
   
    v_x = [i for i in range(min_, max_ + 1)]



stars()
