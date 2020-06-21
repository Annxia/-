#电脑上自动化浏览器需要用到appium????----不需要
#直接使用selenium即可

from selenium import webdriver

#配置浏览器以手机模式启动
chrome_options=webdriver.ChromeOptions()

#选择一种存在的模拟手机设备（分辨率）
chrome_options.add_experimental_option(
    'mobileEmulation',{'deviceName':'iPhone X'}
)
print(type(chrome_options))
#将chrome_optionsz转化成字典
print(type(chrome_options.to_capabilities()))

# driver=webdriver.Chrome(desired_capabilities=chrome_options.to_capabilities())

driver=webdriver.Chrome('C:\Tools\webdriver\chromedriver.exe',desired_capabilities=chrome_options.to_capabilities())

driver.get('http://baidu.com')

driver.find_element_by_id('index-kw').send_keys('松勤\n')

input()

driver.quit()