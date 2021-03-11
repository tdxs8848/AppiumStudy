from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from app.page.BasePage import BasePage
from app.page.EditContactInfoPage import EditContactInfoPage


class EditContactListPage(BasePage):

    #管理通讯录页面
    def click_eidtinfo(self,name):
        self.count  = len(self.finds(MobileBy.XPATH, f"//*[@text='{name}']"))
        # 点击编辑按钮
        self.name = name
        self.find_and_click(MobileBy.XPATH,f"//*[@text='{name}']")
        return EditContactInfoPage(self.driver)

    def verify_ok(self):
        sleep(2)
        try:
            count = len(self.finds(MobileBy.XPATH, f"//*[@text='{self.name}']"))+1
        except:
            count = 0
        if self.count == count:
            return True
        else:
            return False
