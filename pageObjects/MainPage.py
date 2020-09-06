from selenium import webdriver
from selenium.webdriver.support.select import Select


class InstacartCrawler:
    textbox_session_cookie_id="session_cookie"
    textbox_store_id="store"
    select_action_id="action"
    button_retrieve_data='//*[@id="data-retrieval-form"]/button'

    def __init__(self, driver):
        self.driver = driver

    def setSessionCookie(self, sessionCookie):
        self.driver.find_element_by_id(self.textbox_session_cookie_id).clear()
        self.driver.find_element_by_id(self.textbox_session_cookie_id).send_keys(sessionCookie)

    def setStore(self, store):
        self.driver.find_element_by_id(self.textbox_store_id).clear()
        self.driver.find_element_by_id(self.textbox_store_id).send_keys(store)

    def setAction(self, action):
        select = Select(self.driver.find_element_by_id(self.select_action_id))
        select.select_by_visible_text(action)

    def clickButton(self):
        self.driver.find_element_by_xpath(self.button_retrieve_data).click()




