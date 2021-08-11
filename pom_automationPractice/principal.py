# THIS AUTOMATION SCRIPT VERIFY SOME LINKS FROM INDEX PAGE
import unittest
from selenium import webdriver

from pages.pageIndex import PageIndex
from pages.pageContact import PageContact
from pages.pageLogin import PageLogin
from pages.pageSearch import PageSearch
from pages.pageOrder import PageOrder
from pages.pageWomen import PageWomen
from pages.pageDresses import PageDresses
from pages.pageTshirts import PageTshirts
from pages.pageShop import PageShop


class Principal(unittest.TestCase):

    def setUp(self):                                                   
                    # firefox webdriver                    your webdriver path  
        self.driver = webdriver.Firefox(executable_path='/home/.../driverFirefox')
        
        self.driver.get("http://automationpractice.com/index.php")
        self.driver.implicitly_wait(5)
        
        self.pageIndex = PageIndex(self.driver)
        self.pageContact = PageContact(self.driver)
        self.pageLogin = PageLogin(self.driver)
        self.pageSearch = PageSearch(self.driver)
        self.pageOrder = PageOrder(self.driver)
        self.pageWomen = PageWomen(self.driver)
        self.pageDresses = PageDresses(self.driver)
        self.pageTshirts = PageTshirts(self.driver)
        self.pageShop = PageShop(self.driver)

    # Index search box working verification

    def test_search_box_succes(self):             

        self.pageIndex.search_box_input('t-shirt')
        self.pageIndex.submit_button_click()

        self.assertTrue(self.pageSearch.find_combobox(), "Items list is missing")

    def test_search_box_fail(self):

        self.pageIndex.search_box_input('Hello world')
        self.pageIndex.submit_button_click()

        self.assertTrue("No results were found" in self.pageSearch.search_fail_banner(), "Fail banner is missing")

    # Index links working verification

    def test_contact_us(self):                                               

        self.pageIndex.contact_us_click()                                 
        
        self.assertEqual(self.pageContact.title_text(), "CUSTOMER SERVICE - CONTACT US", "Title is missing")

    def test_sign_in(self):                        

        self.pageIndex.sign_in_click() 
       
        self.assertEqual(self.pageLogin.title_text(), "AUTHENTICATION", "Title is missing")    

    def test_cart_link(self):

        self.pageIndex.cart_link_click()

        self.assertEqual(self.pageOrder.title_text(), "SHOPPING-CART SUMMARY", "Title is missing")

    def test_women_link(self):

        self.pageIndex.women_link_click()

        self.assertEqual(self.pageWomen.women_title_text(), 'Women', "Title is missing")

    def test_dresses_link(self):

        self.pageIndex.dresses_link_click()

        self.assertEqual(self.pageDresses.dresses_title_text(), 'Dresses', "Title is missing")

    def test_tshirts_link(self):

        self.pageIndex.tshirts_link_click()

        self.assertEqual(self.pageTshirts.tshirts_title_text(), 'T-shirts', "Title is missing")

    def test_ad_threeDays_link(self):

        self.pageIndex.ad_threeDays_link_click()

        self.assertTrue("PrestaShop" in self.pageShop.title_text(), "Title is missing")
    
    def test_ad_onlyOnline_link(self):

        self.pageIndex.ad_onlyOnline_link_click()

        self.assertTrue("PrestaShop" in self.pageShop.title_text(), "Title is missing")
    
    def tearDown(self):

        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':

    unittest.main(warnings='ignore')



