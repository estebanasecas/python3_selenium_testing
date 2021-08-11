from selenium.webdriver.common.by import By


class PageLogin(object):

    def __init__(self, my_driver):

        self.driver = my_driver

        self.username = (By.ID, 'user-name')
        self.password = (By.ID, 'password')
        self.login_button = (By.ID, 'login-button')
        self.error_banner = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[3]/h3")

    def find_username(self, username):

        self.driver.find_element(*self.username).send_keys(username)

    def find_password(self, password):

        self.driver.find_element(*self.password).send_keys(password)

    def find_login_button(self):

        try:
            return self.driver.find_element(*self.login_button)
           
        except:
            return False

    def login_button_click(self):

        self.driver.find_element(*self.login_button).click()

    def error_banner_text(self):

        return self.driver.find_element(*self.error_banner).text






    
