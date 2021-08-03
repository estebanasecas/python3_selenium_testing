from selenium.webdriver.common.by import By


class PageWomen(object):

    def __init__(self, my_driver):

        self.driver = my_driver

        self.women_title = (By.XPATH, "/html/body/div/div[2]/div/div[3]/div[2]/div[1]/div/div/span")

    def women_title_text(self):

        return self.driver.find_element(*self.women_title).text

        
