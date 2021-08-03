from selenium.webdriver.common.by import By


class PageOrder(object):

    def __init__(self, my_driver):

        self.driver = my_driver

        self.title = (By.ID, "cart_title")

    def title_text(self):

        return self.driver.find_element(*self.title).text


