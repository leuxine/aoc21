
open_ = {'(', '[', '{', '<'}
match = {')' : '(', ']' : '[', '}' : '{', '>' : '<'}


def star1():
    with open('input.in', 'r') as file:
        score = 0
        m = {')' : 3, ']' : 57, '}' : 1197, '>' : 25137}
        for line in file:
            stack = []
            for c in line.strip('\n'):
                if c not in open_:
                    if len(stack) == 0 or stack.pop() != match[c]:
                        score += m[c]
                        break
                else:
                    stack.append(c)

        print("the score for the first star is %d\n" % (score))


def star2():
    with open('input.in', 'r') as file:
        s = {'(' : 1, '[' : 2, '{' : 3, '<' : 4}
        scores = []
        for line in file:
            if line == '\n':
                break

            invalid = False
            stack = []
            for c in line.strip('\n'):
                if c not in open_:
                    if len(stack) == 0 or stack.pop() != match[c]:
                        invalid = True
                        break
                else:
                    stack.append(c)

            if invalid:
                continue

            stack.reverse()
            score = 0
            for c in stack:
                score *= 5
                score += s[c]
           
            scores.append(score)
        
        scores.sort()

        print("the score for the second star is %d\n" % (scores[len(scores)/2]))


star1()
star2()
