filename = 'sample1.txt'



with open(filename) as f_obj:
    lines = f_obj.readlines()


param = lines[0].rstrip().split(' ')

R = param[0]
C = param[1]
L = param[2]
H = param[3]


def findSlice(pizza, xind, yind):
    numT = 0
    numM = 0
    x = xind
    y = yind
    while(numT < L and numM < L and numT + numM < H):
        

pizza = []

for x in range(0, len(lines)):
    lines[x] = lines[x].rstrip()
    if x > 0:
        pizza.append(list(lines[x]))
