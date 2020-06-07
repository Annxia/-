import time

from config import  *

from appium import webdriver

driver=webdriver.Remote('http://localhost:4723/wd/hub',boss_caps)
driver.implicitly_wait(10)

time.sleep(5)

#滑动操作
win_size=driver.get_window_size()
start_x=win_size['width']/2
start_y=win_size['height']/8*7

ele=driver.find_element_by_id('com.hpbr.bosszhipin:id/boss_job_card_view')
#取卡片元素的高度为滑动距离
distance=ele.size['height']
#和屏幕交互，所以滑动的时候注意当前的页面
driver.implicitly_wait(0)
while 1:
    #一边滑动，一边寻找目标元素
    target=driver.find_elements_by_android_uiautomator('new UiSelector().textContains("人工智能")')

    if target:#如果找到元素就退出
        print('找到元素了')
        break
    driver.swipe(start_x, start_y, start_x, start_y - distance)  # 根据滑动的方向选择加减距离-向上就减，向下就增加


driver.implicitly_wait(10)



#


input('...........')
driver.quit()