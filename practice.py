filename = 'sample1.txt'



with open(filename) as f_obj:
    lines = f_obj.readlines()


param = lines[0].rstrip().split(' ')

R = param[0]
C = param[1]
L = param[2]
H = param[3]

slices = []


def findSlice(pizza, xind, yind):
    numT = 0
    numM = 0
    x = xind + 1
    y = yind + 1
    while(numT + numM < H):
        while(numT < L or numM < L):
            for n in range(xind, x):
                for m in range(yind, y):
                    if(pizza[n][m] == "T"):
                        numT += 1
                    elif(pizza[n][m] == "M"):
                        numM += 1
                    else:
                        print("error counting Ts and Ms")
            x += 1
            y += 1
    return (xind, yind, x, y)


pizza = []

for x in range(0, len(lines)):
    lines[x] = lines[x].rstrip()
    if x > 0:
        pizza.append(list(lines[x]))


firstSlice = findSlice(pizza, 0, 0)
slices.append(firstSlice)


print(len(slices))
for pslice in slices:
    print(pslice[0] + " " + pslice[1] + " " + pslice[2] + " " + pslice[3] + " ")
