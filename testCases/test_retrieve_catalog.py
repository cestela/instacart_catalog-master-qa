import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from pageObjects.MainPage import InstacartCrawler
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



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
        self.driver = setup
        self.driver.get(self.baseURL)
        self.instacartCrawler = InstacartCrawler(self.driver)
        self.instacartCrawler.setSessionCookie(self.sessionCookie)
        self.instacartCrawler.setStore(self.store)
        self.instacartCrawler.setAction(self.action)
        self.instacartCrawler.clickButton()
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