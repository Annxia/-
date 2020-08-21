#操作yaml
import yaml

yamlDir = '../data/test.yaml'
yamlDir2 = '../data/api2.yaml'
#创建文件对象
fo = open(yamlDir, 'r', encoding='utf-8')
# res = yaml.load(fo, Loader=yaml.FullLoader)
# print(res)

# 2组数据
res = yaml.load_all(fo, Loader=yaml.FullLoader)
print(res)
for one in res:
    print(one)

fo2 = open(yamlDir2,'w',encoding='utf-8')
data1 = {'name':'tom','age':20}
data2 = [10,20,30,{'name':'tom','age':20}]
yaml.dump(data2,fo2) #写一组数据
yaml.dump_all([data1,data2],fo2) #写多个数据

fo.close()
fo2.close()