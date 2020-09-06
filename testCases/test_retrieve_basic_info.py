import pytest
from pageObjects.MainPage import InstacartCrawler
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_CorrectBasicInfoRetrieval:

    baseURL = ReadConfig.getApplicationURL()
    store = ReadConfig.getStore()
    sessionCookie = ReadConfig.getSessionCookie()
    action = "Retrieve basic info"
    expected_bodyText = ['Wegmans',
                         'https://d2d8wwwkmhfcva.cloudfront.net/156x/d2lnr5mha7bycj.cloudfront.net/warehouse/logo/231/6347ea31-64ed-43c4-991b-7433b2d74bda.png']
    logger = LogGen.loggen()


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_correctBasicInfo(self,setup):
        self.logger.info("----------------- TC_08_CorrectBasicInfo -----------------")
        self.logger.info("***************** Verifying Correct Basic Info Retrieval *****************")
        self.execute_instacartCrawler(setup)
        self.assert_result()

    def assert_result(self):
        actual_bodyText = self.driver.find_element_by_xpath("/html/body/pre").text
        if all(x in actual_bodyText for x in self.expected_bodyText):
            self.driver.close()
            self.logger.info("***************** Correct Basic Info Retrieval Test - PASSED *****************")
            assert True
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_correctBasicInfo.png")
            self.driver.close()
            self.logger.error("***************** Correct Basic Info Retrieval Test - FAILED *****************")
            assert False

    def execute_instacartCrawler(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.instacartCrawler = InstacartCrawler(self.driver)
        self.instacartCrawler.setSessionCookie(self.sessionCookie)
        self.instacartCrawler.setStore(self.store)
        self.instacartCrawler.setAction(self.action)
        self.instacartCrawler.clickButton()