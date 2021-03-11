from appium.webdriver.common.mobileby import MobileBy

from app.page.BasePage import BasePage


class EditContactInfoPage(BasePage):
    #编辑个人信息页面
    def click_delmember(self):
        self.find_and_click(MobileBy.XPATH,"//*[@text='删除成员']")
        self.find_and_click(MobileBy.XPATH,'//*[@text="确定"]')

