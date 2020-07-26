from task.pylib.other import Father
from robot.api import logger


class Child(Father):
    def __init__(self):
        super().__init__()
        logger.console('初始化子类')

    def use_money(self):
        self.money -= 500
        logger.console(f'还剩{self.money}元')