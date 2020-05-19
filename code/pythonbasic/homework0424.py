def getName(srcStr):
    name = srcStr.split(',')[1].split("the name is")[1]
    return name


a = 'A girl come in, the name is Jack, level 955'
b = 'A old lady come in, the name is Mary, level 94454'
c = 'A pretty boy come in, the name is Patrick, level 194'
print(getName(a))
print(getName(b))
print(getName(c))
