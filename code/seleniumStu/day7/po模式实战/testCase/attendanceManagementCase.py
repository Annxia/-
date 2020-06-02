import socket
import time
import unittest

from seleniumStu.day7.po模式实战.pages.attendanceManagementPage import AttendanceManagementPageActionObj as AMPO


class AttendanceManagementCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        前置条件，访问到页面网址
        :return:
        """
        AMPO.to_page()

    def test_punch_clock(self):
        """
        打卡功能测试用例,打卡状态，数据逻辑的正确性，建议放在接口测试中执行
        打卡成功后，新增一条打卡记录，并且打卡记录的内容正确
        :return:
        """
        """ 1 打卡 """
        # 点击打卡按钮
        AMPO.punchClock()
        # 获取本地日期
        local_time = time.localtime()
        # 刷新页面
        AMPO.driver.refresh()

        """ 2 获取最新一行打卡记录的日期 """
        # 获取打卡日期，具体到天
        punch_date = AMPO.sign_table_date_boxes()[0].text
        # 获取打卡时间，具体到秒(去掉最后一位秒数，避免打卡误差)
        punch_time = AMPO.sign_table_time_boxes()[0].text[:-1]
        # 获取打卡状态
        punch_status = AMPO.sign_table_status_boxes()[0].text
        # 获取打卡ip
        punch_ip = AMPO.sign_table_ip_boxes()[0].text

        """ 3 断言 """
        self.assertEqual(punch_date, time.strftime("%Y-%m-%d", local_time), msg="断言打卡日期，具体到天")
        self.assertEqual(punch_time, time.strftime("%H:%M:%S", local_time)[:-1], msg="断言打卡日期，具体到秒(去掉最后一位)")
        self.assertIn(punch_status, ["正常", "迟到", "早退", "加班"], msg="断言打卡状态,不会显示预期之外的状态")
        self.assertIn(punch_ip, self.__get_ip(), msg="断言打卡ip")

    @classmethod
    def __get_ip(cls):
        """
        获取本地 ip,生成一个 UDP 包,把自己的 ip 放到 UDP的协议头里边，然后从 UDP包中获取本地ip
        :return:
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect("8.8.8.8", 80)
        ip = s.getsockname()[0]
        s.close()
        return ip


if __name__ == '__main__':
    unittest.main()
