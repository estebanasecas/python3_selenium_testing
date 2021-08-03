from selenium.webdriver.common.by import By


class PageShop(object):

    def __init__(self, my_driver):

        self.driver = my_driver

        self.title = (By.XPATH, "/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/h1")

    def title_text(self):

        return self.driver.find_element(*self.title).text
