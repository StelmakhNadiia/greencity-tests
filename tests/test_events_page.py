import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GreenCityEventsTests(unittest.TestCase):

    def setUp(self):
      
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.greencity.cx.ua/#/greenCity/events")
        self.wait = WebDriverWait(self.driver, 10)

    def test_page_title(self):
        """Перевірка заголовка сторінки"""
        header = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h1")))
        self.assertIn("Events", header.text)

    def test_search_display(self):
        """Перевірка наявності поля пошуку"""
        search_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Search']")))
        self.assertTrue(search_input.is_displayed())

    def test_negative_search(self):
        """Негативний тест: пошук неіснуючої події"""
        search_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Search']")))
        search_input.send_keys("AbraKadabra123")
        

        no_data = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "no-data")))
        self.assertTrue(no_data.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
