import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Blog_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):
        user = "instructor"
        pwd = "instructor1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://3900team1.pythonanywhere.com/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        time.sleep(3)
        driver.get("http://3900team1.pythonanywhere.com/admin")
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[4]/table/tbody/tr[1]/td[2]/a").click()
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[2]/table/tbody/tr[1]/th/a").click()
        elem = driver.find_element_by_id("id_name")
        elem.send_keys(" style")
        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/form/div/div/input[1]").click()
        time.sleep(5)
    def tearDown(self):
            self.driver.close()

    if __name__ == "__main__":
        unittest.main()

