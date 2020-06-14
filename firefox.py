
import unittest
import selenium
import selenium.firefoxDriver;
from selenium.webdriver.common.keys import  Keys


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox('\geckdriver.exe')


    def test_searh_in_python_org(self):

        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python",driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results foound" not in driver.page_source

    def tearDown(self):

        self.driver.close()

if _name_ == "_main_":
        unittest.main()


























