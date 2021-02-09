from hyrobot.common import *
class c1:
    name = '管理员首页 ui-0101'

    def teststeps(self):
        STEP(1,'登录网站')
        from selenium import webdriver
        driver = webdriver.Chrome(r"F:\chromedriver\chromedriver.exe")

        driver.implicitly_wait(5)
        # ------------------------
        driver.get('http://127.0.0.1/mgr/sign.html')

        driver.find_element_by_id("username").send_keys('byhy')
        driver.find_element_by_id("password").send_keys('88888888\n')
        STEP(2, '获取左侧菜单')
        rr1 = driver.find_elements_by_css_selector('.sidebar-menu  span')

        aa = []
        for span in rr1:
            aa.append(span.text)
            INFO(span.text)
        STEP(3,'左侧菜单是否正确')

        CHECK_POINT("侧边栏是否正确",
            aa[0:3] == ['客户', '药品', '订单'])
        driver.quit()