
import pytest
from pageObjects.MainPage import InstacartCrawler
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_ErrorStore:
    base_url = ReadConfig.getApplicationURL()
    session_cookie = ReadConfig.getSessionCookie()
    store = ReadConfig.getIncorrectValue()
    action_catalog = "Retrieve catalog"
    action_basicinfo = "Retrieve basic info"
    expected_body_text = ['Wegmans',
                         'https://d2d8wwwkmhfcva.cloudfront.net/156x/d2lnr5mha7bycj.cloudfront.net/warehouse/logo/231/6347ea31-64ed-43c4-991b-7433b2d74bda.png']
    error_404 = "Response http code 404 != 200. Are you sure you are using a valid session token?"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_null_store_basicinfo(self, setup):
        self.logger.info("----------------- TC_05_NullStore_BasicInfo -----------------")
        self.logger.info("***************** Verifying Null Store for Basic Info action *****************")
        actual_bodyText = self.load_body(setup, session_cookie=self.session_cookie, action=self.action_basicinfo)

        if all(x in actual_bodyText for x in self.expected_body_text):
            self.driver.close()
            self.logger.info("***************** Null Store (Basic Info) Test - PASSED *****************")
            assert True
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_null_store_basicinfo.png")
            self.driver.close()
            self.logger.error("*****************  Null Store (Basic Info) Test- FAILED *****************")
            assert False

    @pytest.mark.regression
    def test_incorrect_store_basicinfo(self, setup):
        self.logger.info("----------------- TC_06__IncorrectStore_BasicInfo -----------------")
        self.logger.info("***************** Verifying Incorrect Store for Basic Info action *****************")
        actual_body_text = self.load_body(setup, self.session_cookie, self.store, self.action_basicinfo)
        if all(x in actual_body_text for x in self.expected_body_text):
            self.driver.close()
            self.logger.info(
                "***************** Incorrect Store (Basic Info) Test - PASSED *****************")
            assert True
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_incorrect_store_basicinfo.png")
            self.driver.close()
            self.logger.error(
                "*****************  Incorrect Store (Basic Info) Test- FAILED *****************")
            assert False


    @pytest.mark.regression
    def test_null_store_catalog(self, setup):
        self.logger.info("----------------- TC_11_NullStore_Catalog -----------------")
        self.logger.info("***************** Verifying Null Store for Catalog action *****************")
        actual_body_text = self.load_body(setup, session_cookie=self.session_cookie, action=self.action_catalog)
        if actual_body_text == self.error_404:
            self.driver.close()
            self.logger.info("***************** Null Store (Catalog) Test - PASSED *****************")
            assert True
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_null_store_catalog.png")
            self.driver.close()
            self.logger.error("*****************  Null Store (Catalog) Test- FAILED *****************")
            assert False

    @pytest.mark.regression
    def test_incorrect_store_catalog(self, setup):
        self.logger.info("----------------- TC_12_IncorrectStore_Catalog -----------------")
        self.logger.info("***************** Verifying Incorrect Store for Catalog action *****************")
        actual_body_text = self.load_body(setup, self.session_cookie, self.store, self.action_catalog)
        if actual_body_text == self.error_404:
            self.driver.close()
            self.logger.info("***************** Incorrect Store (Catalog) Test - PASSED *****************")
            assert True
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_incorrect_store_catalog.png")
            self.driver.close()
            self.logger.error("*****************  Incorrect Store (Catalog) Test- FAILED *****************")
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