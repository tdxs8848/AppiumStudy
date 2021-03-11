from appium.webdriver.common.mobileby import MobileBy

from app.page.BasePage import BasePage
from app.page.EditContactPage import EditContactPage


class AddContactPage(BasePage):
    def addcontact_menual(self):
        # 手动输入添加
        self.find(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        return EditContactPage(self.driver)
