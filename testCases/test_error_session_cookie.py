import pytest
from pageObjects.MainPage import InstacartCrawler
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_ErrorSessionCookie:
    base_url = ReadConfig.getApplicationURL()
    store = ReadConfig.getStore()
    session_cookie = ReadConfig.getIncorrectValue()
    action_catalog = "Retrieve catalog"
    action_basicinfo = "Retrieve basic info"
    error_500 = "Can't find basic info in the response HTML. Are you sure you're using a valid session token?"
    error_401 = "Response http code 401 != 200. Are you sure you are using a valid session token?"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_null_sessioncookie_basicinfo(self, setup):
        self.logger.info("----------------- TC_01_NullSessionCookie_BasicInfo -----------------")
        self.logger.info("***************** Verifying Null Session Cookie for Basic Info action *****************")
        actual_body_text = self.load_body(setup, store=self.store, action=self.action_basicinfo)
        if actual_body_text == self.error_500:
            self.driver.close()
            self.logger.info("***************** Null Session Cookie (Basic Info) Test - PASSED *****************")
            assert True
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_null_sessioncookie_basicinfo.png")
            self.driver.close()
            self.logger.error("***************** Null Session Cookie (Basic Info) Test - FAILED *****************")
            assert False

    @pytest.mark.regression
    def test_incorrect_sessioncookie_basicinfo(self, setup):
        self.logger.info("----------------- TC_02_IncorrectSessionCookie_BasicInfo -----------------")
        self.logger.info("***************** Verifying Incorrect Session Cookie for Basic Info action *****************")
        actual_body_text = self.load_body(setup, self.session_cookie, self.store, self.action_basicinfo)
        if actual_body_text == self.error_500:
            self.driver.close()
            self.logger.info("***************** Incorrect Session Cookie (Basic Info) Test - PASSED *****************")
            assert True
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_incorrect_sessioncookie_basicinfo.png")
            self.driver.close()
            self.logger.error("***************** Incorrect Session Cookie (Basic Info) Test - FAILED *****************")
            assert False

    @pytest.mark.regression
    def test_null_sessioncookie_catalog(self, setup):
        self.logger.info("----------------- TC_03_NullSessionCookie_Catalog -----------------")
        self.logger.info("***************** Verifying Null Session Cookie for Catalog action *****************")
        actual_body_text = self.load_body(setup, store=self.store, action=self.action_catalog)
        if actual_body_text == self.error_401:
            self.driver.close()
            self.logger.info("***************** Null Session Cookie (Catalog) Test - PASSED *****************")
            assert True
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_null_sessioncookie_catalog.png")
            self.driver.close()
            self.logger.error("***************** Null Session Cookie (Catalog) Test - FAILED *****************")
            assert False


    @pytest.mark.regression
    def test_incorrect_sessioncookie_catalog(self, setup):
        self.logger.info("----------------- TC_04_IncorrectSessionCookie_Catalog -----------------")
        self.logger.info("***************** Verifying Incorrect Session Cookie for Catalog action *****************")
        actual_body_text = self.load_body(setup, self.session_cookie, self.store, self.action_catalog)
        if actual_body_text == self.error_401:
            self.driver.close()
            self.logger.info("***************** Incorrect Session Cookie (Catalog) Test - PASSED *****************")
            assert True
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_incorrect_sessioncookie_catalog.png")
            self.driver.close()
            self.logger.error("***************** Incorrect Session Cookie (Catalog) Test - FAILED *****************")
            assert False

    def load_body(self, setup, session_cookie=None, store=None, action=None):
        self.driver = setup
        self.driver.get(self.base_url)
        self.instacartCrawler = InstacartCrawler(self.driver)
        if session_cookie is not None:
            self.instacartCrawler.setSessionCookie(session_cookie)
        if store is not None:
            self.instacartCrawler.setStore(store)
        if action is not None:
            self.instacartCrawler.setAction(action)
        self.instacartCrawler.clickButton()
        actual_body_text = self.driver.find_element_by_xpath("/html/body").text
        return actual_body_text
