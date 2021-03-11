from time import sleep

from app.page.app import App


class TestContact:
    def setup_class(self):
        self.app = App().start()

    def setup(self):
        self.mian = self.app.goto_main()

    def teardown_class(self):
        sleep(2)
        self.app.stop()

    def test_addcontact(self):
        name = "ccc"
        phonenum = "13400000590"
        editpage = self.mian.goto_addresslist().click_addcontact().addcontact_menual()
        editpage.edit_contact(name,phonenum)
        editpage.verify_ok()

    def test_delcontact(self):
        name = "ccc"
        editPage = self.mian.goto_addresslist().click_editcontact()
        editPage.click_eidtinfo(name).click_delmember()
        assert editPage.verify_ok()
