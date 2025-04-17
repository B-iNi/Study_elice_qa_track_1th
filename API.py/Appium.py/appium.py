from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import unittest


class SimpleTest(unittest.TestCase):
    def setUp(self):
        options = AppiumOptions()
        options.load_capabilities(
            {
                "platformName": "Android",
                "appium:deviceName": "emulator-5554",
                "appium:automationName": "UiAutomator2",
            }
        )
        self.driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
        print("Appium Driver Created")

    def test_search_input(self):
        try:
            search_box_id = "com.android.chrome:id/search_box_text"
            wait = WebDriverWait(self.driver, 10)
            search_input = wait.until(
                EC.presence_of_element_located((AppiumBy.ID, search_box_id))
            )
            expected_text = "Test Input"
            search_input.send_keys(expected_text)

            url_bar_id = "com.android.chrome:id/url_bar"
            url_bar = wait.until(EC.element_to_be_clickable((AppiumBy.ID, url_bar_id)))

            actual_text = url_bar.text
            self.assertEqual(
                actual_text,
                expected_text,
                f"Assertion Failed:Expected text'${expected_text} but got '${actual_text}",
            )
            print("Assertion passed:Input text matches expected text.")

            suggestion_xpath = f"//android.widget.TextView[@resource-id='com.android.chrome:id/line_1' and @text='{expected_text}']"
            suggestion_element = wait.until(
                EC.element_to_be_clickable((AppiumBy.XPATH, suggestion_xpath))
            )
            suggestion_element.click()

            result_page_search_xpath = (
                f"//android.widget.EditText[@text='{expected_text}']"
            )
            result_element = wait.until(
                EC.visibility_of_element_located(
                    (AppiumBy.XPATH, result_page_search_xpath)
                )
            )
            self.assertTrue(
                result_element.is_displayed(),
                f"Element with '{expected_text}' not displayed on result page.",
            )
            print("Assertion passed:element is displayed")

            home_button_id = "com.android.chrome:id/home_button"
            home_button = wait.until(
                EC.element_to_be_clickable((AppiumBy.ID, home_button_id))
            )
            home_button.click()
            print("test completed")
        except Exception as e:
            print(e)
            raise

    def tearDown(self):
        if self.driver:
            self.driver.quit()
