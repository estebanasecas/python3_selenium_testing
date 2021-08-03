from selenium.webdriver.common.by import By


class PageSearch(object):

    def __init__(self, my_driver):

        self.driver = my_driver

        self.sort_by_combobox = (By.ID, 'selectProductSort')
        self.fail_banner = (By.XPATH, "/html/body/div/div[2]/div/div[3]/div[2]/p")
    
    def find_combobox(self):

        try:
            return self.driver.find_element(*self.sort_by_combobox)

        except:             
            return False

    def search_fail_banner(self):

        return self.driver.find_element(*self.fail_banner).text

    
