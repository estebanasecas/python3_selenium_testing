from selenium.webdriver.common.by import By


class PageSauceLabs(object):

    def __init__(self, my_driver):

        self.driver = my_driver

        self.sauce_lab_icon_link = (By.XPATH, "/html/body/header/div/nav/div/a")
    
    def find_sauce_lab_icon_link(self):  

        try:
            return self.driver.find_element(*self.sauce_lab_icon_link)

        except:
            return False

        
                   





