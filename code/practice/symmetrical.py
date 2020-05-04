def is_symmertrical(num):
    length = len(num)

    if length % 2 == 1:
        num = num[:length//2] + num[length//2+1:]

    part1 = num[:length//2]
    part2 = num[length//2:]

    return part1 == part2[::-1]

while True:
    num = input("请输入一个数字：")
    print(is_symmertrical(num))