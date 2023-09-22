from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Resources_Reader.Locator_Reader import locate_element


class CommonActions:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Adjust the timeout as needed
            
    

    def wait_for_element_to_be_visible(self, locator_name):
        element = locate_element(locator_name)
        try:
            self.wait.until(EC.visibility_of_element_located(element))
        except Exception as e:
            print(f"Element not visible: {e}")

    def click_element(self, locator_name):
        element = locate_element(locator_name)
        try:
            self.wait.until(EC.element_to_be_clickable(element)).click()
        except Exception as e:
            print(f"Element not clickable: {e}")

    def enter_text(self, locator_name, text):
        element = locate_element(locator_name)
        try:
            self.wait.until(EC.presence_of_element_located(element)).send_keys(text)
        except Exception as e:
            print(f"Unable to enter text: {e}")

    def get_text(self, locator_name):
        element = locate_element(locator_name)
        try:
            return self.wait.until(EC.presence_of_element_located(element)).text
        except Exception as e:
            print(f"Unable to get text: {e}")
            return None

    def is_element_displayed(self, locator_name):
        element = locate_element(locator_name)
        try:
            return self.wait.until(EC.presence_of_element_located(element)).is_displayed()
        except Exception as e:
            print(f"Element not displayed: {e}")
            return False

    def is_element_enabled(self, locator_name):
        element = locate_element(locator_name)
        try:
            return self.wait.until(EC.presence_of_element_located(element)).is_enabled()
        except Exception as e:
            print(f"Element not enabled: {e}")
            return False

    def wait_for_element_visibility(self, locator_name):
        element = locate_element(locator_name)
        try:
            self.wait.until(EC.visibility_of_element_located(element))
        except Exception as e:
            print(f"Element not visible: {e}")

    def wait_for_element_to_be_clickable(self, locator_name):
        element = locate_element(locator_name)
        try:
            self.wait.until(EC.element_to_be_clickable(element)).click()
        except Exception as e:
            print(f"Element not clickable: {e}")

    def switch_to_frame(self, frameName):
        try:
            self.driver.switch_to.frame(frameName)
        except Exception as e:
            print(f"Unable to switch to frame: {e}")

    def switch_to_default_content(self):
        try:
            self.driver.switch_to.default_content()
        except Exception as e:
            print(f"Unable to switch to default content: {e}")

    def take_screenshot(self, screenshotPath):
        try:
            self.driver.save_screenshot(screenshotPath)
            print("Screenshot saved to:", screenshotPath)
        except Exception as e:
            print(f"Unable to take screenshot: {e}")

    def select_option_by_visible_text(self, dropdown_locator_name, visibleText):
        element = locate_element(dropdown_locator_name)
        try:
            self.click_element(dropdown_locator_name)
            option_locator = f"//option[text()='{visibleText}']"
            self.click_element((By.XPATH, option_locator))
        except Exception as e:
            print(f"Unable to select option by visible text: {e}")

    def select_option_by_value(self, dropdown_locator_name, value):
        element = locate_element(dropdown_locator_name)
        try:
            self.click_element(dropdown_locator_name)
            option_locator = f"//option[@value='{value}']"
            self.click_element((By.XPATH, option_locator))
        except Exception as e:
            print(f"Unable to select option by value: {e}")

    def select_option_by_index(self, dropdown_locator_name, index):
        element = locate_element(dropdown_locator_name)
        try:
            self.click_element(dropdown_locator_name)
            option_locator = f"//option[{index + 1}]"
            self.click_element((By.XPATH, option_locator))
        except Exception as e:
            print(f"Unable to select option by index: {e}")