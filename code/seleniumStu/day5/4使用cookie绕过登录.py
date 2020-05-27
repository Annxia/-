
cookieSli = [
    {'domain': '.baidu.com',
     # 'expiry': 1849611146.572706,
     'httpOnly': True,
     'name': 'BDUSS',
     'path': '/',
     'secure': False,
     'value': 'J-RlpoUUUxWmx6ZTJBOE55UGxsM0FHY3BCOHBEZXp0ODAtU2txaGJsdUtUUE5lRVFBQUFBJCQAAAAAAAAAAAEAAAC998szsLLpd8LlAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIq~y16Kv8teRU'
     },
    {'domain': '.baidu.com',
     'httpOnly': False,
     'name': 'H_PS_PSSID',
     'path': '/',
     'secure': False,
     'value': '31730_1465_21123_31660_31464_30824_26350_22159'
     },
    {'domain': '.www.baidu.com',
     # 'expiry': 2536491148,
     'httpOnly': False,
     'name': 'sugstore',
     'path': '/',
     'secure': False,
     'value': '1'
     },
    {'domain': '.baidu.com',
     # 'expiry': 1621947109.031051,
     'httpOnly': False,
     'name': 'BAIDUID',
     'path': '/',
     'secure': False,
     'value': '8e53412a540ff7b5560bc24cd2c1aef8:FG=1'
     },
    {'domain': '.baidu.com',
     # 'expiry': 3737894756.030948,
     'httpOnly': False,
     'name': 'BIDUPSID',
     'path': '/',
     'secure': False,
     'value': '8e53412a540ff7b5560bc24cd2c1aef8'
     },
    {'domain': '.baidu.com',
     # 'expiry': 3737894756.031023,
     'httpOnly': False,
     'name': 'PSTM',
     'path': '/',
     'secure': False,
     'value': '1590411109'
     },
    {'domain': 'www.baidu.com',
     # 'expiry': 1591275148,
     'httpOnly': False,
     'name': 'BD_UPN',
     'path': '/',
     'secure': False,
     'value': '12314753'
     },
    {'domain': 'www.baidu.com',
     'httpOnly': False,
     'name': 'BD_HOME',
     'path': '/',
     'secure': False,
     'value': '1'
     },
]

from selenium import webdriver

# 创建一个浏览器驱动对象
driver = webdriver.Chrome(r"E:\Program Files\JetBrains\PyCharm 2019.3.3\bin\chromedriver.exe")

# 访问网址
driver.get("http://www.baidu.com")

for cook in cookieSli:
    driver.add_cookie(cook)
driver.refresh()