from functools import reduce

def process(binary):
    
    if len(binary) < 11:
        return 0

    #print(binary)
    
    v = int(binary[:3], 2)
    t = int(binary[3:6], 2)

    if t == 4:
        #print("literal value version %d\n" % v)
        tmp = 6
        while tmp < len(binary) and int(binary[tmp],2) == 1:
            tmp += 5
        
        if tmp >= len(binary):
            return v

        return v + process(binary[tmp+5:])
    else:
        #print("operator packet version %d\n" % v)
        l_id = binary[6]
        if int(l_id,2) == 0:
            #num_bits = int(binary[7:22], 2)
            return v + process(binary[22:])
        else:
            #num_pack = int(binary[7:18], 2)
            return v + process(binary[18:])

    
def compute(binary):
    
    if len(binary) < 11:
        return 0

    t = int(binary[3:6], 2)

    if t == 4:
        val = '0b' 
        tmp = 6
        while int(binary[tmp],2) == 1:
            val += binary[tmp+1:tmp+5]
            tmp += 5
        
        val += binary[tmp+1:tmp+5]
        # ignoring this case
        #if tmp >= len(binary):
        #    return v

        binary = binary[tmp+5:]

        return int(val, 2), binary
    else:
        l_id = binary[6]
        op_list = []
        if int(l_id,2) == 0:
            num_bits = int(binary[7:22], 2)
            binary = binary[22:]
            diff = len(binary) - num_bits
            while len(binary) > diff:
                val, binary = compute(binary)
                op_list.append(val)
        else:
            num_pack = int(binary[7:18], 2)
            binary = binary[18:]
            for i in range(num_pack):
                val, binary = compute(binary)
                op_list.append(val)
        
        if t == 0:
            return sum(op_list), binary
        elif t == 1:
            return reduce(lambda x, y: x * y, op_list), binary
        elif t == 2:
            return min(op_list), binary
        elif t == 3:
            return max(op_list), binary
        elif (t == 5 and op_list[0] > op_list[1]) or (t == 6 and \
                op_list[0] < op_list[1]) or (t == 7 and op_list[0] == op_list[1]):
            return 1, binary
        else:
            return 0, binary

def stars(star):
    stream = ""
    with open('input.in', 'r') as file:
        hex_stream = file.readline().strip('\n')

    num_bits = len(hex_stream) * 4
    binary = bin(int(hex_stream, 16))[2:].zfill(num_bits)

    print(hex_stream)
    print(binary)

    if star == 1:
        print(process(binary)) 
    else:
        res, tmp = compute(binary)
        print(res)


#stars(1)
stars(2)
