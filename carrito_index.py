

class CarritoIndex:
    self.query_top = 'search_query_top'
    self.query_button = 'submit_search'
    self.driver = my_driver


    def search(self, item):
        self.driver.find_element_by_id(self.query_top).send_keys('t-shirts')
        self.driver.find_element_by_name(self.query_button).click()

     def seleciona_color(self, item):

        self.driver.find_element_by_id('color_1')
        self.driver.find_element_by_name(self.query_button).click()

     # hacer click 25 veces

     def agregar_carrito(self, item):

          self.driver.find_element_by_id(self.query_top('25'))
          self.driver.find_element_by_class('icon-plus')


            int i=0

            while(i <=4)
            self.driver.find_element_by_class(self.query_button.click())
            i ++

    # verificar numero = 25

    self.assertEqual(self.driver.find_element_by_id('quantity_wanted)', '28')













