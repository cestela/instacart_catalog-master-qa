import pytest
from pageObjects.MainPage import InstacartCrawler
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_CorrectCatalogRetrieval:
    base_url = ReadConfig.getApplicationURL()
    store = ReadConfig.getStore()
    session_cookie = ReadConfig.getSessionCookie()
    action = "Retrieve catalog"

    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_correct_catalog(self, setup):
        self.logger.info("----------------- TC_09_CorrectCatalog -----------------")
        self.logger.info("***************** Verifying Correct Catalog Retrieval *****************")
        actual_body_text = self.load_body(setup, self.session_cookie, self.store, self.action)
        self.assert_result(actual_body_text)

    def assert_result(self, actual_body_text):
        if len(actual_body_text) > 0:
            self.driver.close()
            self.logger.info("***************** Correct Catalog Retrieval Test - PASSED *****************")
            assert True
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_correctCatalog.png")
            self.driver.close()
            self.logger.error("***************** Correct Catalog Retrieval Test - FAILED *****************")
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
