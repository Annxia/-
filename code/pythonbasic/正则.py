import re

str1 = '145abc18759564256<>>dsfffs15'
res = re.findall('\d{11}',str1)
print(res)

# str1 = 'a\nb  1    2'
# res = re.findall('\S',str1)
# print(res)

# str1 = 'ab12_#45'
# res = re.findall('\W',str1)
# res1 = re.findall('\W{3}',str1)
# print(res,'\n',res1)

# str1 = '''{"data":"abcd"}'''
# res = re.findall('"data":"(.*?)"',str1)
# print(res)

# str1 = 'songqinsn'
# res = re.findall('so+n',str1)
# print(res)

# str1 = 'songqinsn'
# res = re.findall('so*n',str1)
# print(res)

# str1 = 'songqins\n'
# res = re.findall('s.',str1)
# print(res)