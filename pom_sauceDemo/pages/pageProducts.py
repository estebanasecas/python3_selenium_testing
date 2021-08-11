from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class PageProducts(object):

    def __init__(self, my_driver):

        self.driver = my_driver

        self.title = (By.XPATH, "/html/body/div/div/div/div[1]/div[2]/span")
        self.combobox = (By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div[2]/span/select")
        self.items_name = (By.CLASS_NAME, "inventory_item_name")
        self.items_price = (By.CLASS_NAME, "inventory_item_price")
        self.shop_cart = (By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[3]/a")
        self.menu_button = (By.ID, "react-burger-menu-btn")
        self.menu_button_list = (By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/nav")
        self.menu_button_list_all_items = (By.ID, "inventory_sidebar_link")
        self.menu_button_list_about = (By.ID, "about_sidebar_link")
        self.menu_button_list_logout = (By.ID, "logout_sidebar_link") 
        self.menu_button_list_reset_app_state = (By.ID, "reset_sidebar_link")

    def title_text(self):

        return self.driver.find_element(*self.title).text

    def combobox_search_by_index(self, index):

        combobox = Select(self.driver.find_element(*self.combobox))

        combobox.select_by_index(index)    
    #
    def items_name_array_actual(self):

        items_name = []

        all_items = self.driver.find_elements(*self.items_name)

        for i in all_items:

             items_name.append(i.text)

        return items_name    
    #
    def items_name_array_sorted(self):

        items_name = []
        all_items = self.driver.find_elements(*self.items_name)

        for i in all_items:
             items_name.append(i.text)

        sorted_items_name = sorted(items_name)        
        return sorted_items_name
    #
    def items_name_array_sorted_rev(self):

        items_name = []
        all_items = self.driver.find_elements(*self.items_name)

        for i in all_items:
             items_name.append(i.text)

        rev_sorted_items_name = sorted(items_name, reverse=True)        
        return rev_sorted_items_name
    #
    def items_price_array_actual(self):

        items_price = []

        all_items = self.driver.find_elements(*self.items_price)

        for i in all_items:
            
            price_string = i.text
            number_string = price_string.replace('$','')
            number_float = float(number_string)
            items_price.append(number_float)

        return items_price
    #
    def items_price_array_sorted(self):

        items_price = []

        all_items = self.driver.find_elements(*self.items_price)

        for i in all_items:
            
            price_string = i.text
            number_string = price_string.replace('$','')
            number_float = float(number_string)
            items_price.append(number_float)
                                
        items_price_sorted = sorted(items_price)
        return items_price_sorted        
    #
    def items_price_array_sorted_rev(self):

        items_price = []

        all_items = self.driver.find_elements(*self.items_price)

        for i in all_items:
            
            price_string = i.text
            number_string = price_string.replace('$','')
            number_int = float(number_string)
            items_price.append(number_int)
                                
        items_price_sorted_rev = sorted(items_price, reverse=True)
        return items_price_sorted_rev    
    #
    def shop_cart_button_click(self):

        self.driver.find_element(*self.shop_cart).click()
    #
    def menu_button_click(self):

        self.driver.find_element(*self.menu_button).click()
    #
    def menu_button_list_displayed(self):

        menu_button_list = self.driver.find_element(*self.menu_button_list)
        return menu_button_list.is_displayed()                
    #
    def menu_button_list_all_items_click(self):

        self.driver.find_element(*self.menu_button_list_all_items).click()
    #
    def menu_button_list_about_click(self):

        self.driver.find_element(*self.menu_button_list_about).click()
    #
    def menu_button_list_logout_click(self):

        self.driver.find_element(*self.menu_button_list_logout).click()
    #
    def menu_button_list_reset_app_state_click(self):

        self.driver.find_element(*self.menu_button_list_reset_app_state).click()
    







        
