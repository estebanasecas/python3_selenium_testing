# THIS AUTOMATION SCRIPT VERIFY SOME WEB-ELEMENTS FROM LOGIN AND PRINCIPAL PAGE 
import unittest
from selenium import webdriver

from pages.pageLogin import PageLogin 
from pages.pageProducts import PageProducts            
from pages.pageShopCart import PageShopCart                                              
from pages.pageSauceLabs import PageSauceLabs


class Principal(unittest.TestCase):

    def setUp(self):
                    # firefox webdriver                    your webdriver path  
        self.driver = webdriver.Firefox(executable_path='/home/.../driverFirefox')

        self.driver.get("https://www.saucedemo.com/")
        self.driver.implicitly_wait(5)

        self.pageLogin = PageLogin(self.driver)
        self.pageProducts = PageProducts(self.driver)
        self.pageShopCart = PageShopCart(self.driver)
        self.pageSauceLabs = PageSauceLabs(self.driver)

    def test_login(self):

        self.pageLogin.find_username('standard_user')
        self.pageLogin.find_password('secret_sauce')
        self.pageLogin.login_button_click()

        self.assertEqual(self.pageProducts.title_text(), 'PRODUCTS', 'Error login')
        
    def test_login_fail(self):

        self.pageLogin.find_username('hello_world')
        self.pageLogin.find_password('abc12345')
        self.pageLogin.login_button_click()

        self.assertTrue("Epic sadface" in self.pageLogin.error_banner_text(), 'Error fail_login')

    def test_combobox_index0(self):                                                                          # COMBOBOX

        self.pageLogin.find_username('standard_user')
        self.pageLogin.find_password('secret_sauce')
        self.pageLogin.login_button_click()
     
        self.pageProducts.combobox_search_by_index(0)       

        self.assertEqual(self.pageProducts.items_name_array_actual(),
                         self.pageProducts.items_name_array_sorted(), "Error combobox")  

    def test_combobox_index1(self):                                                     

        self.pageLogin.find_username('standard_user')
        self.pageLogin.find_password('secret_sauce')
        self.pageLogin.login_button_click()
     
        self.pageProducts.combobox_search_by_index(1)       

        self.assertEqual(self.pageProducts.items_name_array_actual(),
                         self.pageProducts.items_name_array_sorted_rev(), "Error combobox") 

    
    def test_combobox_index2(self):                                                     

        self.pageLogin.find_username('standard_user')
        self.pageLogin.find_password('secret_sauce')
        self.pageLogin.login_button_click()
     
        self.pageProducts.combobox_search_by_index(2) 

        self.assertEqual(self.pageProducts.items_price_array_actual(),
                         self.pageProducts.items_price_array_sorted(), "Error combobox")

    def test_combobox_index3(self):                                                     

        self.pageLogin.find_username('standard_user')
        self.pageLogin.find_password('secret_sauce')
        self.pageLogin.login_button_click()
     
        self.pageProducts.combobox_search_by_index(3) 

        self.assertEqual(self.pageProducts.items_price_array_actual(),
                         self.pageProducts.items_price_array_sorted_rev(), "Error combobox")

    def test_shop_cart(self):                                                                                # SHOP CART

        self.pageLogin.find_username('standard_user')
        self.pageLogin.find_password('secret_sauce')
        self.pageLogin.login_button_click()     

        self.pageProducts.shop_cart_button_click()

        self.assertEqual(self.pageShopCart.title_text(), "YOUR CART", "Error shop cart")

    def test_menu_button(self):                                                                             # MENU BUTTON

        self.pageLogin.find_username('standard_user')
        self.pageLogin.find_password('secret_sauce')
        self.pageLogin.login_button_click() 

        self.pageProducts.menu_button_click()    

        self.assertTrue(self.pageProducts.menu_button_list_displayed(), "Error menu button")

    def test_menu_button_list_all_items(self):

        self.pageLogin.find_username('standard_user')
        self.pageLogin.find_password('secret_sauce')
        self.pageLogin.login_button_click() 

        self.pageProducts.menu_button_click()    
        self.pageProducts.menu_button_list_all_items_click()
 
        self.assertEqual(self.pageProducts.title_text(), "PRODUCTS", "Error menu button All_items")

    def test_menu_button_list_about(self):

        self.pageLogin.find_username('standard_user')
        self.pageLogin.find_password('secret_sauce')
        self.pageLogin.login_button_click() 

        self.pageProducts.menu_button_click()    
        self.pageProducts.menu_button_list_about_click()

        self.assertTrue(self.pageSauceLabs.find_sauce_lab_icon_link(), "Error menu button About")

    def test_menu_button_list_logout(self):

        self.pageLogin.find_username('standard_user')
        self.pageLogin.find_password('secret_sauce')
        self.pageLogin.login_button_click() 

        self.pageProducts.menu_button_click()    
        self.pageProducts.menu_button_list_logout_click()

        self.assertTrue(self.pageLogin.find_login_button(), "Error menu button Logout")

    def test_menu_button_list_reset_app_state(self):

        self.pageLogin.find_username('standard_user')
        self.pageLogin.find_password('secret_sauce')
        self.pageLogin.login_button_click() 

        self.pageProducts.menu_button_click()    
        self.pageProducts.menu_button_list_reset_app_state_click()
 
        self.assertEqual(self.pageProducts.title_text(), "PRODUCTS", "Error menu button Reset_app_state")               
    
    def tearDown(self):

        self.driver.close()
        self.driver.quit() 



if __name__ == "__main__":

    unittest.main(warnings='ignore')   


