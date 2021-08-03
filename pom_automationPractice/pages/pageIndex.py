from selenium.webdriver.common.by import By


class PageIndex(object):

    def __init__(self, my_driver):

        self.driver = my_driver

        self.contact_us_link = (By.LINK_TEXT, "Contact us")
        self.sign_in_link = (By.LINK_TEXT, "Sign in")

        self.search_box = (By.ID, "search_query_top")
        self.submit_button = (By.NAME, "submit_search")                

        self.cart_link = (By.XPATH, "/html/body/div/div[1]/header/div[3]/div/div/div[3]/div/a")

        self.women_link = (By.LINK_TEXT, "WOMEN")
        self.dresses_link = (By.LINK_TEXT, "DRESSES")
        self.tshirts_link = (By.LINK_TEXT, "T-SHIRTS")

        self.ad_excepteur_link = (By.XPATH, "/html/body/div/div[2]/div/div[1]/div/div[1]/div/div[1]/ul/li[3]/a/img")
        self.ad_threeDays_link = (By.XPATH, "/html/body/div/div[2]/div/div[1]/div/div[2]/ul/li[1]/a/img")
        self.ad_onlyOnline_link = (By.XPATH, "/html/body/div/div[2]/div/div[1]/div/div[2]/ul/li[2]/a/img")

    def contact_us_click(self):

        self.driver.find_element(*self.contact_us_link).click() 

    def sign_in_click(self):

        self.driver.find_element(*self.sign_in_link).click()

    def search_box_input(self, my_item):

        search_box = self.driver.find_element(*self.search_box)
        search_box.send_keys(my_item)
     
    def submit_button_click(self):

        self.driver.find_element(*self.submit_button).click()

    def cart_link_click(self):

        self.driver.find_element(*self.cart_link).click()

    def women_link_click(self):

        self.driver.find_element(*self.women_link).click()
     
    def dresses_link_click(self):

        self.driver.find_element(*self.dresses_link).click()
        
    def tshirts_link_click(self):

        self.driver.find_element(*self.tshirts_link).click()
    
    def ad_threeDays_link_click(self):

        self.driver.find_element(*self.ad_threeDays_link).click()

    def ad_onlyOnline_link_click(self):

        self.driver.find_element(*self.ad_onlyOnline_link).click()







