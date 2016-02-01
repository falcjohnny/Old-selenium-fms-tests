# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestCreateDelSnapFirefox(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(command_executor='http://172.17.0.3:4444/wd/hub',desired_capabilities=DesiredCapabilities.FIREFOX)
        self.driver.implicitly_wait(30)
        self.base_url = "http://172.22.12.197/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_create_del_snap_firefox(self):
        driver = self.driver
        driver.find_element_by_xpath("//li[3]/a/span").click()
        driver.find_element_by_xpath("//button[@type='button']").click()
        for i in range(60):
            try:
                if driver.find_element_by_xpath("//button[@type='submit']").is_displayed(): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_name("totalSize").clear()
        driver.find_element_by_name("totalSize").send_keys("2048")
        for i in range(60):
            try:
                if driver.find_element_by_css_selector("h5.modal-title").is_displayed(): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        for i in range(60):
            try:
                if driver.find_element_by_xpath("//div[@id='center']/div/div[2]/div[2]/div/div/div/div").is_displayed(): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_xpath("//div[@id='center']/div/div[2]/div[2]/div/div/div/div").click()
        driver.find_element_by_xpath("//div[4]/button").click()
        driver.find_element_by_link_text("Create Snapshot Resource").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        for i in range(60):
            try:
                if driver.find_element_by_xpath("//div[@id='center']/div/div[2]/div[2]/div/div/div/div").is_displayed(): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_xpath("//div[@id='center']/div/div[2]/div[2]/div/div/div/div").click()
        driver.find_element_by_xpath("//div[4]/button").click()
        driver.find_element_by_link_text("Snapshot Resource").click()
        driver.find_element_by_xpath("//li[7]/a/span").click()
        for i in range(60):
            try:
                if driver.find_element_by_xpath("//button[@type='submit']").is_displayed(): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        for i in range(60):
            try:
                if driver.find_element_by_xpath("//div[@id='center']/div/div[2]/div[2]/div/div/div/div").is_displayed(): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        # Delet SAN Resource
        driver.find_element_by_xpath("//div[@id='center']/div/div[2]/div[2]/div/div/div/div").click()
        driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
        for i in range(60):
            try:
                if driver.find_element_by_xpath("//button[@type='submit']").is_displayed(): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
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
