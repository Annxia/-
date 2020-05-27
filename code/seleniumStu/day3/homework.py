import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_driver = r"E:\Program Files\JetBrains\PyCharm 2019.3.3\bin\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)
driver.implicitly_wait(10)
driver.get("https://www.51job.com")

driver.find_element_by_xpath("//*/div[3]/div/div[1]/div/a").click()
driver.find_element_by_id("kwdselectid").send_keys("Python")
driver.find_element_by_id("work_position_input").click()
# locations = driver.find_elements_by_id("work_position_click_center_right_list_000000")
locations = driver.find_elements_by_css_selector("#work_position_click_center_right_list_000000 em[class=on]")
for loc in locations:
    time.sleep(2)
    loc.click()

driver.find_element_by_id("work_position_click_center_right_list_category_000000_080200").click()
driver.find_element_by_id("work_position_click_bottom_save").click()

# 控件遮挡？？这一句是抄作业里面的，下一句的funtype_click click才能正常运行,求解释，没看懂
driver.find_element_by_css_selector(".rtit.r1").click()
driver.find_element_by_css_selector("#funtype_click").click()
# driver.find_element_by_xpath('//*[@id="funtype_click"]').click()
# WebDriverWait(driver,10).until(EC.visibility_of_element_located(By.ID("funtype_click")))

ele = driver.find_element_by_id("funtype_click_center_left_each_0100")
ActionChains(driver).move_to_element(ele).perform()
# 选择职能类别：计算机软件 -> 高级软件工程师
driver.find_element_by_id("funtype_click_center_right_list_category_0100_0100").click()
driver.find_element_by_id("funtype_click_center_right_list_sub_category_each_0100_0106").click()
driver.find_element_by_id("funtype_click_bottom_save").click()
# 选择公司性质：外资(欧美)
# driver.find_element_by_id("cottype_list").click()
# driver.find_element_by_xpath('//*[@id="cottype_list"]/div/span[3]').click()
# 选择工作年限：1-3年
driver.find_element_by_id("workyear_list").click()
driver.find_element_by_xpath('//*[@id="workyear_list"]/div/span[3]').click()
driver.find_element_by_css_selector("div.btnbox.p_sou > span").click()

results = driver.find_elements_by_css_selector("#resultList div.el")

for res in results[1:]:
    jobs = res.find_elements_by_tag_name("span")
    # 这样打印出来每行最后也会也有 |
    # for job in jobs:
    #     text = job.text
    #     print(text, end='|')
    # print(" ")

    print('|'.join(info.text for info in jobs))


driver.quit()