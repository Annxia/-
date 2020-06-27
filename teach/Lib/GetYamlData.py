import json
from pprint import pprint

import yaml
def get_yaml_data():
    yamlDir = '../data/api.yaml'
    fo = open(yamlDir,'r', encoding='utf-8')
    res = yaml.load(fo, Loader=yaml.FullLoader)
    # pprint(res)

    # 封装数据
    resList =[]
    for one in res:
        resList.append((json.dumps(one['data'],ensure_ascii=False), json.dumps(one['check'],ensure_ascii=False)))
    # print(resList)
    return resList


if __name__ == '__main__':
    get_yaml_data()

#https://120.55.190.222/mgr/login/login.html