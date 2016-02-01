# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestAddServerAssignCustomerFirefox(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(command_executor='http://172.17.0.3:4444/wd/hub',desired_capabilities=DesiredCapabilities.FIREFOX)
        self.driver.implicitly_wait(30)
        self.base_url = "http://172.17.0.2/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_server_assign_customer_firefox(self):
        driver = self.driver
        driver.get(self.base_url + "/#/login")
        for i in range(60):
            try:
                if driver.find_element_by_css_selector("span.ng-binding").is_displayed(): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_xpath("//input[@type='text']").clear()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("superadmin")
        driver.find_element_by_xpath("//input[@type='password']").clear()
        driver.find_element_by_xpath("//input[@type='password']").send_keys("freestor")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//li[5]/a/span").click()
        driver.find_element_by_link_text("Manage Servers").click()
        driver.find_element_by_xpath("//button[@type='button']").click()
        driver.find_element_by_name("ipAddress").clear()
        driver.find_element_by_name("ipAddress").send_keys("172.22.5.140")
        driver.find_element_by_name("userName").clear()
        driver.find_element_by_name("userName").send_keys("root")
        driver.find_element_by_name("passwd").clear()
        driver.find_element_by_name("passwd").send_keys("IPStor101")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//li[3]/div/span").click()
        driver.find_element_by_xpath("//button[@type='button']").click()
        driver.find_element_by_xpath("(//input[@type='text'])[2]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys("test")
        driver.find_element_by_xpath("(//input[@type='text'])[3]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[3]").send_keys("test.com")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
        driver.find_element_by_xpath("//fieldset/div/div/div/div/span").click()
        # Select server to assign it to customer
        driver.find_element_by_link_text("FSSVA-H5-140").click()
        driver.find_element_by_xpath("//label[contains(.,'Shared')]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[4]").click()
        # Select the Storage Pool
        driver.find_element_by_xpath("//span[contains(.,'OpenStack-StoragePool-1')]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("(//a[contains(@href, '')])[8]").click()
        driver.find_element_by_link_text("Logout").click()
        driver.find_element_by_xpath("//input[@type='text']").clear()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("admin")
        driver.find_element_by_xpath("(//input[@type='text'])[2]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys("test.com")
        driver.find_element_by_xpath("//input[@type='password']").clear()
        driver.find_element_by_xpath("//input[@type='password']").send_keys("freestor")
        driver.find_element_by_xpath("//button[@type='submit']").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
