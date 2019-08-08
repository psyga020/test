import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Blog_ATS(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_blog(self):
       user = "a"
       pwd = "123456789a"
       driver = self.driver
       driver.maximize_window()
       driver.get("http://127.0.0.1:8000/admin")
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       time.sleep(3)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       time.sleep(3)
       elem.send_keys(Keys.RETURN)
       time.sleep(3)
       driver.get("http://127.0.0.1:8000")
       assert "Logged In"
       time.sleep(5)

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()
