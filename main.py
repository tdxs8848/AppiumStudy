from appium import webdriver
caps = {}
caps["platformName"] = "android"
caps["deviceName"] = "mumu"
caps["appPackage"] = "com.tencent.wework"
caps["appActivity"] = ".launch.LaunchSplashActivity"
caps["noReset"] = "true"
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[@text="通讯录"]').click()
driver.find_element_by_xpath('//*[@text="添加成员"]').click()
driver.find_element_by_xpath('//*[@text="手动输入添加"]').click()
driver.find_element_by_xpath('//*[@text="必填"]').send_keys('cg')
driver.find_element_by_xpath('//*[@text="必填"]').send_keys('13424405199')
driver.find_element_by_xpath('//*[@text="保存"]').click()
