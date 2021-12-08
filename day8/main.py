

def star1():

    with open('input.in', 'r') as file:
        count = 0
        for line in file:
            words = line.strip('\n').replace('|', ' ').split()
            digits = words[-4:]

            for d in digits:
                if len(d) == 2 or len(d) == 4 or \
                        len(d) == 3 or len(d) == 7:
                            count += 1

        print("number of 1,4,7,8s is %d\n" % (count))

def star2():
            
    with open('input.in', 'r') as file:
        count = 0
        for line in file:
            if line == '\n':
                break
            words = line.strip('\n').replace('|', ' ').split()
            digits = words[:10]
            input_ = words[-4:]

            digits.sort(key=len)

            maybe_cf = [c for c in digits[0]]

            a = [c for c in digits[1] if c not in maybe_cf] 
            sure_a = a[0]

            maybe_f1 = [c for c in digits[6] if c in maybe_cf]
            maybe_f2 = [c for c in digits[7] if c in maybe_cf]
            maybe_f3 = [c for c in digits[8] if c in maybe_cf]


            sure_f = '\0'
            if len(maybe_f1) < len(maybe_f2):
                if len(maybe_f1) < len(maybe_f3):
                    sure_f = maybe_f1[0]
                else:
                    sure_f = maybe_f3[0]
            else:
                if len(maybe_f2) < len(maybe_f3):
                    sure_f = maybe_f2[0]
                else:
                    sure_f = maybe_f3[0]

            sure_c = maybe_cf[0] if maybe_cf[0] != sure_f else maybe_cf[1]

            maybe_bd = [c for c in digits[2] if c not in maybe_cf]

            maybe_b1 = [c for c in digits[6] if c in maybe_bd]
            maybe_b2 = [c for c in digits[7] if c in maybe_bd]
            maybe_b3 = [c for c in digits[8] if c in maybe_bd]

            sure_b = '\0' 
            if len(maybe_b1) < len(maybe_b2):
                if len(maybe_b1) < len(maybe_b3):
                    sure_b = maybe_b1[0]
                else:
                    sure_b = maybe_b3[0]
            else:
                if len(maybe_b2) < len(maybe_b3):
                    sure_b = maybe_b2[0]
                else:
                    sure_b = maybe_b3[0]

            sure_d = maybe_bd[0] if maybe_bd[0] != sure_b else maybe_bd[1]

            abcdf = [sure_a, sure_b, sure_c, sure_d, sure_f]

            maybe_g1 = [c for c in digits[3] if c not in abcdf]
            maybe_g2 = [c for c in digits[4] if c not in abcdf]
            maybe_g3 = [c for c in digits[5] if c not in abcdf]

            sure_g = '\0'
            sure_e = '\0'
            if len(maybe_g1) == len(maybe_g2):
                sure_g = maybe_g1[0]
                sure_e = maybe_g3[0] if maybe_g3[0] != sure_g else maybe_g3[1]
            elif len(maybe_g1) == len(maybe_g3):
                sure_g = maybe_g1[0]
                sure_e = maybe_g2[0] if maybe_g2[0] != sure_g else maybe_g2[1]
            else:
                sure_g = maybe_g2[0]
                sure_e = maybe_g1[0] if maybe_g1[0] != sure_g else maybe_g1[1]


            num = []
            for w in input_:
                if len(w) == 2:
                    num.append(1)
                elif len(w) == 3:
                    num.append(7)
                elif len(w) == 4:
                    num.append(4)
                elif len(w) == 7:
                    num.append(8)
                elif len(w) == 5:
                    if sure_e in w:
                        num.append(2)
                    elif sure_b in w:
                        num.append(5)
                    else:
                        num.append(3)
                elif len(w) == 6:
                    if sure_d not in w:
                        num.append(0)
                    elif sure_c not in w:
                        num.append(6)
                    else:
                        num.append(9)

            res = 0
            ten = 10**(len(num) - 1)
            for n in num:
                res += n * ten
                ten /= 10

            count += res

            print(digits)
            print(input_)
            mappings = [sure_a, sure_b, sure_c, sure_d, sure_e, sure_f, sure_g]
            print(mappings)
            print("the number is %d\n" % (res))
        
        print("the final result is %d\n" % (count))

star1()
star2()
