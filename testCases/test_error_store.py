
import pytest
from pageObjects.MainPage import InstacartCrawler
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_ErrorStore:
    baseURL = ReadConfig.getApplicationURL()
    sessionCookie = ReadConfig.getSessionCookie()
    store = ReadConfig.getIncorrectValue()
    actionCatalog = "Retrieve catalog"
    actionBasicInfo = "Retrieve basic info"
    expected_bodyText = ['Wegmans',
                         'https://d2d8wwwkmhfcva.cloudfront.net/156x/d2lnr5mha7bycj.cloudfront.net/warehouse/logo/231/6347ea31-64ed-43c4-991b-7433b2d74bda.png']
    error_404 = "Response http code 404 != 200. Are you sure you are using a valid session token?"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_nullStore_BasicInfo(self, setup):
        self.logger.info("----------------- TC_05_NullStore_BasicInfo -----------------")
        self.logger.info("***************** Verifying Null Store for Basic Info action *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.instacartCrawler = InstacartCrawler(self.driver)
        self.instacartCrawler.setSessionCookie(self.sessionCookie)
        self.instacartCrawler.setAction(self.actionBasicInfo)
        self.instacartCrawler.clickButton()
        actual_bodyText = self.driver.find_element_by_xpath("/html/body/pre").text

        if all(x in actual_bodyText for x in self.expected_bodyText):
            self.driver.close()
            self.logger.info("***************** Null Store (Basic Info) Test - PASSED *****************")
            assert True
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_nullStore_BasicInfo.png")
            self.driver.close()
            self.logger.error("*****************  Null Store (Basic Info) Test- FAILED *****************")
            assert False

    @pytest.mark.regression
    def test_incorrectStore_BasicInfo(self, setup):
        self.logger.info("----------------- TC_06__IncorrectStore_BasicInfo -----------------")
        self.logger.info("***************** Verifying Incorrect Store for Basic Info action *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.instacartCrawler = InstacartCrawler(self.driver)
        self.instacartCrawler.setSessionCookie(self.sessionCookie)
        self.instacartCrawler.setStore(self.store)
        self.instacartCrawler.setAction(self.actionBasicInfo)
        self.instacartCrawler.clickButton()

        actual_bodyText = self.driver.find_element_by_xpath("/html/body/pre").text
        if all(x in actual_bodyText for x in self.expected_bodyText):
            self.driver.close()
            self.logger.info(
                "***************** Previous Search > Incorrect Store (Basic Info) Test - PASSED *****************")
            assert True
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_previousSearch_incorrectStore_BasicInfo.png")
            self.driver.close()
            self.logger.error(
                "*****************  Previous Search > Incorrect Store (Basic Info) Test- FAILED *****************")
            assert False


    @pytest.mark.regression
    def test_nullStore_Catalog(self, setup):
        self.logger.info("----------------- TC_11_NullStore_Catalog -----------------")
        self.logger.info("***************** Verifying Null Store for Catalog action *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.instacartCrawler = InstacartCrawler(self.driver)
        self.instacartCrawler.setSessionCookie(self.sessionCookie)
        self.instacartCrawler.setAction(self.actionCatalog)
        self.instacartCrawler.clickButton()
        actual_bodyText = self.driver.find_element_by_xpath("/html/body").text
        if actual_bodyText == self.error_404:
            self.driver.close()
            self.logger.info("***************** Null Store (Catalog) Test - PASSED *****************")
            assert True
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_nullStore_Catalog.png")
            self.driver.close()
            self.logger.error("*****************  Null Store (Basic Info) Test- FAILED *****************")
            assert False

    @pytest.mark.regression
    def test_incorrectStore_Catalog(self, setup):
        self.logger.info("----------------- TC_12_IncorrectStore_Catalog -----------------")
        self.logger.info("***************** Verifying Incorrect Store for Catalog action *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.instacartCrawler = InstacartCrawler(self.driver)
        self.instacartCrawler.setSessionCookie(self.sessionCookie)
        self.instacartCrawler.setStore(self.store)
        self.instacartCrawler.setAction(self.actionCatalog)
        self.instacartCrawler.clickButton()
        actual_bodyText = self.driver.find_element_by_xpath("/html/body").text
        if actual_bodyText == self.error_404:
            self.driver.close()
            self.logger.info("***************** Incorrect Store (Catalog) Test - PASSED *****************")
            assert True
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_incorrectStore_Catalog.png")
            self.driver.close()
            self.logger.error("*****************  Incorrect Store (Basic Info) Test- FAILED *****************")
            assert False