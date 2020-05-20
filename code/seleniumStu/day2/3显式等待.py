
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 创建一个浏览器驱动对象
driver = webdriver.Chrome(r"E:\Program Files\JetBrains\PyCharm 2019.3.3\bin\chromedriver.exe")

# 访问网址
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("松勤\n")

# driver.find_element_by_link_text("松勤软件测试_腾讯课堂").click()
# 每隔0.5秒检查一次，最多等待 10 秒
WebDriverWait(driver, 10, 0.5).until(
    EC.visibility_of_element_located(
        (By.LINK_TEXT, "松勤软件测试_腾讯课堂")
    )
)

driver.quit()