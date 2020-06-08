# 域名
DoMAIN = "http://127.0.0.1:8088/"

# 超时时间
TIMEOUT = 10

# 轮询时间
POLL_FREQUENCY = 0.5

# driver路径
driverPath = {
    "Chrome": r"D:\Program Files (x86)\Python\chromedriver.exe",
    "Firefox": r"D:\geckodriver.exe"
}

# cookie 过期后需更新
cookieSli = [
    {'domain': '127.0.0.1',
     'httpOnly': False,
     'name': 'Hm_lpvt_750463144f16fe69eb3ac11bea1c4436',
     'path': '/',
     'secure': False,
     'value': '1590754997'},
    {'domain': '127.0.0.1',
     # 'expiry': 1622290997,
     'httpOnly': False,
     'name': 'Hm_lvt_750463144f16fe69eb3ac11bea1c4436',
     'path': '/',
     'secure': False,
     'value': '1590754981'},
    {'domain': '127.0.0.1',
     # 'expiry': 1622290980,
     'httpOnly': True,
     'name': 'beegosessionID',
     'path': '/',
     'secure': False,
     'value': '4b74c469fddf720968b3b9100a7d2e31'}
]
