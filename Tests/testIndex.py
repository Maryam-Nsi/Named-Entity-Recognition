import unittest
from selenium import webdriver

class E2ETests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=r'/Applications/geckodriver')
        self.driver.get('http://localhost:5000')

    def tearDown(self):
        self.driver.quit()

    def testTitle(self):
        self.assertIn('Named Entity', self.driver.title)

    def testHeading(self):
        heading = self._find("heading").text
        self.assertEqual('Named Entity Finder', heading)

    def testInput(self):
        input_element = self._find('input-text')
        self.assertIsNotNone(input_element)

    def testSubmitting(self):
        submit_button = self._find('find-button')
        self.assertIsNotNone(submit_button)

    def testTable(self):
        input_element = self._find('input-text')
        submit_button = self._find('find-button')
        input_element.send_keys('London is a great city in England.')
        submit_button.click()
        table = self._find('ner-table')
        self.assertIsNotNone(table)

    def _find(self, val):
        return self.driver.find_element_by_css_selector(f'[data-test-id="{val}"]')

