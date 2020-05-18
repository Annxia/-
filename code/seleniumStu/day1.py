from selenium import webdriver

driver = webdriver.Chrome(r"E:\Program Files\JetBrains\PyCharm 2019.3.3\bin\chromedriver.exe")

driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("Python")
driver.find_element_by_id("su").click()
driver.quit()