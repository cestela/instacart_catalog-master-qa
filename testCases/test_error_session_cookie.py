import pytest
from pageObjects.MainPage import InstacartCrawler
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_ErrorSessionCookie:
    baseURL = ReadConfig.getApplicationURL()
    store = ReadConfig.getStore()
    sessionCookie = ReadConfig.getIncorrectValue()
    actionCatalog = "Retrieve catalog"
    actionBasicInfo = "Retrieve basic info"
    error_500 = "Can't find basic info in the response HTML. Are you sure you're using a valid session token?"
    error_401 = "Response http code 401 != 200. Are you sure you are using a valid session token?"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_nullSessionCookie_BasicInfo(self, setup):
        self.logger.info("----------------- TC_01_NullSessionCookie_BasicInfo -----------------")
        self.logger.info("***************** Verifying Null Session Cookie for Basic Info action *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.instacartCrawler = InstacartCrawler(self.driver)
        self.instacartCrawler.setStore(self.store)
        self.instacartCrawler.setAction(self.actionBasicInfo)
        self.instacartCrawler.clickButton()
        actual_bodyText = self.driver.find_element_by_xpath("/html/body").text
        if actual_bodyText == self.error_500:
            self.driver.close()
            self.logger.info("***************** Null Session Cookie (Basic Info) Test - PASSED *****************")
            assert True
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_nullSessionCookie_BasicInfo.png")
            self.driver.close()
            self.logger.error("***************** Null Session Cookie (Basic Info) Test - FAILED *****************")
            assert False

    @pytest.mark.regression
    def test_incorrectSessionCookie_BasicInfo(self, setup):
        self.logger.info("----------------- TC_02_IncorrectSessionCookie_BasicInfo -----------------")
        self.logger.info("***************** Verifying Incorrect Session Cookie for Basic Info action *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.instacartCrawler = InstacartCrawler(self.driver)
        self.instacartCrawler.setSessionCookie(self.sessionCookie)
        self.instacartCrawler.setStore(self.store)
        self.instacartCrawler.setAction(self.actionBasicInfo)
        self.instacartCrawler.clickButton()
        actual_bodyText = self.driver.find_element_by_xpath("/html/body").text
        if actual_bodyText == self.error_500:
            self.driver.close()
            self.logger.info("***************** Incorrect Session Cookie (Basic Info) Test - PASSED *****************")
            assert True
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_incorrectSessionCookie_BasicInfo.png")
            self.driver.close()
            self.logger.error("***************** Incorrect Session Cookie (Basic Info) Test - FAILED *****************")
            assert False

    @pytest.mark.regression
    def test_nullSessionCookie_Catalog(self, setup):
        self.logger.info("----------------- TC_03_NullSessionCookie_Catalog -----------------")
        self.logger.info("***************** Verifying Null Session Cookie for Catalog action *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.instacartCrawler = InstacartCrawler(self.driver)
        self.instacartCrawler.setStore(self.store)
        self.instacartCrawler.setAction(self.actionCatalog)
        self.instacartCrawler.clickButton()
        actual_bodyText = self.driver.find_element_by_xpath("/html/body").text
        if actual_bodyText == self.error_401:
            self.driver.close()
            self.logger.info("***************** Null Session Cookie (Catalog) Test - PASSED *****************")
            assert True
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_nullSessionCookie_Catalog.png")
            self.driver.close()
            self.logger.error("***************** Null Session Cookie (Catalog) Test - FAILED *****************")
            assert False

    @pytest.mark.regression
    def test_incorrectSessionCookie_Catalog(self, setup):
        self.logger.info("----------------- TC_04_IncorrectSessionCookie_Catalog -----------------")
        self.logger.info("***************** Verifying Incorrect Session Cookie for Catalog action *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.instacartCrawler = InstacartCrawler(self.driver)
        self.instacartCrawler.setSessionCookie(self.sessionCookie)
        self.instacartCrawler.setStore(self.store)
        self.instacartCrawler.setAction(self.actionCatalog)
        self.instacartCrawler.clickButton()
        actual_bodyText = self.driver.find_element_by_xpath("/html/body").text
        if actual_bodyText == self.error_401:
            self.driver.close()
            self.logger.info("***************** Incorrect Session Cookie (Catalog) Test - PASSED *****************")
            assert True
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_incorrectSessionCookie_BasicInfo.png")
            self.driver.close()
            self.logger.error("***************** Incorrect Session Cookie (Catalog) Test - FAILED *****************")
            assert False
