from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class LoginTest(unittest.TestCase):

    def setUp(self):
        # Set up Chrome WebDriver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://the-internet.herokuapp.com/login")  # Public test login page
        time.sleep(2)

    def test_valid_login(self):
        driver = self.driver
        driver.find_element(By.ID, "username").send_keys("tomsmith")  # Correct username
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")  # Correct password
        driver.find_element(By.CSS_SELECTOR, "button.radius").click()  # Login button
        time.sleep(2)

        # Verify successful login (check for 'Secure Area' text)
        self.assertIn("Secure Area", driver.page_source)

    def test_invalid_login(self):
        driver = self.driver
        driver.find_element(By.ID, "username").send_keys("invalid_user")
        driver.find_element(By.ID, "password").send_keys("wrong_password")
        driver.find_element(By.CSS_SELECTOR, "button.radius").click()
        time.sleep(2)

        # Check for error message
        error_msg = driver.find_element(By.ID, "flash").text  # Error message element
        self.assertIn("Your username is invalid!", error_msg)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()