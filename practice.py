filename = 'sample1.txt'



with open(filename) as f_obj:
    lines = f_obj.readlines()


param = lines[0].rstrip().split(' ')

r = param[0]
c = param[1]
l = param[2]
h = param[3]

pizza = []

for x in range(0, len(lines)):
    lines[x] = lines[x].rstrip()
    if x > 0:
        pizza.append(list(lines[x]))

for x in range(0, len(pizza)):
    for y in range(0, len(pizza[x])):
        print(pizza[x][y])
