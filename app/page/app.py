import yaml
from appium import webdriver

from app.page.BasePage import BasePage
from app.page.MainPage import MainPage

with open("../datas/caps.yml") as f:
    datas = yaml.safe_load(f)
    desires = datas['desirecaps']
    ip = datas['server']['ip']
    port = datas['server']['port']


class App(BasePage):
    def start(self):
        if self.driver == None:
            # 启动app
            # 客户端与appium 服务器建立连接的代码
            self.driver = webdriver.Remote(f"http://{ip}:{port}/wd/hub", desires)
            self.driver.implicitly_wait(5)
        else:
            # self.driver.start_activity("com.tencent.wework",".launch.LaunchSplashActivity")
            self.driver.launch_app()
        return self

    def restart(self):
        # 重启app
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):
        # 停止app
        self.driver.quit()

    def goto_main(self):
        return MainPage(self.driver)