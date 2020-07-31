# Generated by Selenium IDE
import shelve
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestTestclass():
  def setup_method(self, method):
    chromenew = Options()
    chromenew.debugger_address = "127.0.0.1:9222"
    self.driver = webdriver.Chrome(options=chromenew)
    self.vars = {}
  
  def test_testclass(self):
    self.driver.get("https://www.baidu.com/index.php?tn=monline_3_dg")
    self.driver.set_window_size(1295, 695)
    self.driver.find_element(By.ID, "kw").click()
    self.driver.find_element(By.ID, "kw").send_keys("霍格沃兹学院")
    self.driver.find_element(By.ID, "kw").send_keys(Keys.ENTER)
    self.vars["window_handles"] = self.driver.window_handles
    time.sleep(2)
    self.driver.find_element(By.LINK_TEXT, "霍格沃兹测试学院 – 测试开发工程师的黄埔军校").click()


  def test_wework(self):
    self.driver.get('https://work.weixin.qq.com/')
    ##先获取到cookies,然后去掉有效期，将cookies存储到db数据库里
    #print(self.driver.get_cookies())
    #打开数据库
    db = shelve.open('cookies')
    #cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688850271618623'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970324950146710'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688850271618623'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'cNVnY72qFCbUNa6DLBaMcAVRVNu3avykNrgxTBo2IjPMjeT9QmtpbWJPa6Etyry3'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a8713257'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'FktiDYTafzscE9je8JaynkmmtqYDN4cBJxhaqtYGpq9yzG32nTqfGVJaUjans0Fcn0t5qaWfCcUfjwauta1ZFQex4l14AXXlu3mjDTcr4EwUhDmO-QWNKhIrSS29qB5B03jL5AOcvBO5zBjNKj9KyMaHK9-wR0JPNF9NBTIUxx_BkPwg0lfzD1-m4QbCmDDbUj-ygvUdqRDC6Wz6aULnUe2GzMwX3SW4R9n0x4Ke4Mkm6hy-bNK9tAlWZ3Os2zV8eeGc9Z1bpcps8cj1SoIdDQ'}, {'domain': '.qq.com', 'expiry': 1658043928, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1113978387.1594971470'}, {'domain': '.work.weixin.qq.com', 'expiry': 1595003003.227876, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 1596334173, 'httpOnly': False, 'name': 'ptui_loginuin', 'path': '/', 'secure': False, 'value': '1083564664@qq.com'}, {'domain': '.qq.com', 'expiry': 2147483648.848916, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': '42e3c24d9e2a8b9bdcdcff8e025d266c861e76d99e01db7de81c215fdddd4ee4'}, {'domain': '.work.weixin.qq.com', 'expiry': 1626507706, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1594971468,1594971559,1594971707'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '8712797775'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.qq.com', 'expiry': 2147483647.607313, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'V8CwALyCY4'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1594971707'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '14198023692267664'}, {'domain': '.qq.com', 'expiry': 1595058328, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.900008405.1594971470'}, {'domain': 'work.weixin.qq.com', 'expiry': 1595003003.227845, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '196nr0'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '6610808832'}, {'domain': '.work.weixin.qq.com', 'expiry': 1597563931.54481, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh-cn'}]
    #进行存储
    #db["cookies"] =cookies
    #读取cookies
    cookies = db["cookies"]
    for cookie in cookies:
      if "expiry" in cookie.keys():
        cookie.pop("expiry")
        #把字典加入到driver的cookies中
        self.driver.add_cookie(cookie)
    self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
    self.driver.find_element(By.ID,'menu_contacts').click()
    #关闭数据库
    db.close()