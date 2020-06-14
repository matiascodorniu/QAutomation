
import unittest
import time

from selenium import webdriver
from pageIndex import PageIndex
from pageItems import  PageItems
from pageItem import PageItem

class SearchCases(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('Chromedriver.exe')
        self.driver.get = ('http://automationpractice.com/index.php')
        self.indexPage = PageIndex(self.driver)
        self.itemsPage = PageItems(driver)

        self.itemsPage = PageItem(self.driver)


    @unittest.skip("not needed now")
    def test_search_no_elements(self):

        self.indexPage.search('hola')

        time.sleep(2)
        self.assertEqual(self.itemsPage.return_no_element_text(),'No results were fouund for your search "hola"')

    @unittest.skip("not needed now")
    def test_search_find_dresses(self):

        self.indexPage.search('dres')
        time.sleep(2)
        self.assertTrue('DRESS' in self.itemsPage.return_section_title())

    @unittest.skip("not needed now")
    def test_search_find_tshirts(self):
        self.indexPage.search('t-shirt')
        time.sleep(2)
        self.assertTrue('T-SHIRT' in self.itemsPage.return_section_title())



    def test_tarea(self):

        self.indexPage.search('t-shirt')
        time.sleep(2)
        self.itemsPage.click_orange_button()
        time.sleep(2)
        self.itemsPage.enter_quantity('25')
        time.sleep(3)

















    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__== '__main__':
    unittest.main()



















