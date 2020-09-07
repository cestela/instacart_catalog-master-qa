import pytest
from pageObjects.MainPage import InstacartCrawler
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_CorrectBasicInfoRetrieval:
    base_url = ReadConfig.getApplicationURL()
    store = ReadConfig.getStore()
    session_cookie = ReadConfig.getSessionCookie()
    action = "Retrieve basic info"
    expected_body_text = ['Wegmans',
                          'https://d2d8wwwkmhfcva.cloudfront.net/156x/d2lnr5mha7bycj.cloudfront.net/warehouse/logo/231'
                          '/6347ea31-64ed-43c4-991b-7433b2d74bda.png']
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_correct_basicinfo(self, setup):
        self.logger.info("----------------- TC_08_CorrectBasicInfo -----------------")
        self.logger.info("***************** Verifying Correct Basic Info Retrieval *****************")
        actual_body_text = self.load_body(setup, self.session_cookie, self.store, self.action)
        self.assert_result(actual_body_text)

    def assert_result(self, actual_body_text):
        if all(x in actual_body_text for x in self.expected_body_text):
            self.driver.close()
            self.logger.info("***************** Correct Basic Info Retrieval Test - PASSED *****************")
            assert True
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_correctBasicInfo.png")
            self.driver.close()
            self.logger.error("***************** Correct Basic Info Retrieval Test - FAILED *****************")
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
