from robot.api import logger
class Father:
    def __init__(self):
        logger.console('初始化父类')

    def make_money(self):
        logger.console('获得10000元')
        self.money=10000