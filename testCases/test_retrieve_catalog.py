import pytest
from pageObjects.MainPage import InstacartCrawler
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen



class Test_CorrectCatalogRetrieval:

    baseURL = ReadConfig.getApplicationURL()
    store = ReadConfig.getStore()
    sessionCookie = ReadConfig.getSessionCookie()
    action = "Retrieve catalog"

    logger = LogGen.loggen()


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_correctCatalog(self,setup):
        self.logger.info("----------------- TC_09_CorrectCatalog -----------------")
        self.logger.info("***************** Verifying Correct Catalog Retrieval *****************")
        self.execute_instacartCrawler(setup)
        self.assert_result()

    def assert_result(self):
        actual_bodyText = self.driver.find_element_by_xpath("/html/body/pre").text.split('",')
        if len(actual_bodyText) > 0:
            self.driver.close()
            self.logger.info("***************** Correct Catalog Retrieval Test - PASSED *****************")
            assert True
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_correctCatalog.png")
            self.driver.close()
            self.logger.error("***************** Correct Catalog Retrieval Test - FAILED *****************")
            assert False

    def execute_instacartCrawler(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.instacartCrawler = InstacartCrawler(self.driver)
        self.instacartCrawler.setSessionCookie(self.sessionCookie)
        self.instacartCrawler.setStore(self.store)
        self.instacartCrawler.setAction(self.action)
        self.instacartCrawler.clickButton()
        self.driver.implicitly_wait(7)