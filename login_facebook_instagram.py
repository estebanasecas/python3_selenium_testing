# THIS AUTOMATION SCRIPT LOGIN YOU IN FACEBOOK AND INSTAGRAM
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Duo(unittest.TestCase):

    def setUp(self):               
                    #      webdriver browser               webdriver path
        self.driver = webdriver.Firefox(executable_path='.../driverFirefox')
        self.driver.implicitly_wait(5)

    def test_duo(self):

        driver = self.driver
        driver.get("http://www.instagram.com")                   

        usuario = driver.find_element_by_name("username")
        usuario.send_keys("instagram_username")                   # modify

        clave = driver.find_element_by_name("password")
        clave.send_keys("instagram_password")                     # modify
        clave.send_keys(Keys.ENTER)
       
        driver.execute_script("window.open('');")               

        driver.switch_to.window(driver.window_handles[1])
        driver.get("http://www.facebook.com")

        usuario2 = driver.find_element_by_id("email")
        usuario2.send_keys("facebook_email")                      # modify

        clave2 = driver.find_element_by_id("pass")                
        clave2.send_keys("facebook_password")                     # modify
        
        clave2.send_keys(Keys.ENTER)

        driver.switch_to.window(driver.window_handles[0])      



if __name__ == "__main__":

    unittest.main()   




















