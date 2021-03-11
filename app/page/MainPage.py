# 主页
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from app.page.AddresslistPage import AddressListPage
from app.page.BasePage import BasePage


class MainPage(BasePage):
    addresslist_element = (MobileBy.XPATH, "//*[@text='通讯录']")

    def goto_addresslist(self):
        # 点击 通讯录
        self.find(*self.addresslist_element).click()
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        return AddressListPage(self.driver)
