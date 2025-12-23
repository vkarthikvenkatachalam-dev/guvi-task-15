from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self,driver):
        self.driver=driver
        self.username=(By.XPATH,"//input[@placeholder='Username']")
        self.password=(By.XPATH,"//input[@placeholder='Password']")
        self.login_button=(By.XPATH,"//button[@type='submit']")
        self.dashboard_header=(By.XPATH,"//h6[(text()='Dashboard')]")
    def login(self,username,password):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located(self.username)).send_keys(username)
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located(self.password)).send_keys(password)
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.login_button)).click()
    def is_login_successful(self):
        try:
            WebDriverWait(self.driver,5).until(EC.presence_of_element_located(self.dashboard_header))
            return True
        except:
            return False