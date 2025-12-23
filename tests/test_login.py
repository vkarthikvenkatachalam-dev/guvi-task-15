from selenium import webdriver

from pages.login_page import LoginPage
from utils.excel_utils import get_test_data, update_result

excel_file="my_files/login_data.xlsx"
test_data =get_test_data(excel_file)
def make_test(test_id, username, password):
    def _test():
        driver = webdriver.Edge()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.maximize_window()

        login_page = LoginPage(driver)
        login_page.login(username, password)

        result = "Passed" if login_page.is_login_successful() else "Failed"
        update_result(excel_file, test_id, result)

        driver.quit()
    return _test

for test_id, username, password in test_data:
    globals()[f"test_login_{test_id}"] = make_test(test_id, username, password)


