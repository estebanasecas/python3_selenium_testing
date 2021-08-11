from selenium.webdriver.common.by import By


class PageShopCart(object):

    def __init__(self, my_driver):

        self.driver = my_driver

        self.title = (By.XPATH, "/html/body/div/div/div/div[1]/div[2]/span")

    def title_text(self):

        return self.driver.find_element(*self.title).text    

