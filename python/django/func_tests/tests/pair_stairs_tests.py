from unittest.case import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestPairStairs(TestCase):
    def test_should_create_pair_stairs_from_list_of_names(self):
        # Go to page
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8000/create')
        self.assertEqual(self.driver.title, "Create a new pair stair")
        # Enter Names
        element = self.driver.find_element(By.CSS_SELECTOR, '#programmer_names')
        element.send_keys('Mickey Mouse')
        # Submit
        self.driver.find_element(By.CSS_SELECTOR, '#add_programmers').click()

        # Assert Pair Stairs is displayed
        self.assertEqual(self.driver.title, 'Pair Stairs')

        stairs = self.driver.find_element(By.CSS_SELECTOR, '#stairs')
        self.assertIn('Mickey Mouse', stairs.text)
        raise NotImplementedError("You still need to write this!")

    def tearDown(self):
        self.driver.close()


