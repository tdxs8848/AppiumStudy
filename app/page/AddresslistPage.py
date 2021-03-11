from appium.webdriver.common.mobileby import MobileBy

from app.page.AddcontactPage import AddContactPage
from app.page.BasePage import BasePage
from app.page.EditContactListPage import EditContactListPage


class AddressListPage(BasePage):


    def click_addcontact(self):
        element = self.swipe_find("添加成员")
        element.click()
        return AddContactPage(self.driver)

    def click_editcontact(self):
        self.find_and_click(MobileBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout[2]/android.widget.TextView")
        return EditContactListPage(self.driver)