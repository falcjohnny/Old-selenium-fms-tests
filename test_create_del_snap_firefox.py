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
        self.base_url = "http://172.17.0.2/"
	self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_create_del_snap_firefox(self):
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
        driver.find_element_by_link_text("Servers").click()
        for i in range(60):
            try:
                if driver.find_element_by_xpath("//button[@type='button']").is_displayed(): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_xpath("//button[@type='button']").click()
        driver.find_element_by_name("ipAddress").clear()
        driver.find_element_by_name("ipAddress").send_keys("172.22.5.140")
        driver.find_element_by_name("userName").clear()
        driver.find_element_by_name("userName").send_keys("root")
        driver.find_element_by_name("passwd").clear()
        driver.find_element_by_name("passwd").send_keys("IPStor101")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        for i in range(60):
            try:
                if driver.find_element_by_xpath("//strong[contains(.,'Server added')]").is_displayed(): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        # Go to Customer
        driver.find_element_by_xpath("//li[3]/div/span").click()
        driver.find_element_by_xpath("//button[@type='button']").click()
        driver.find_element_by_xpath("(//input[@type='text'])[2]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys("test")
        driver.find_element_by_xpath("(//input[@type='text'])[3]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[3]").send_keys("test.com")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        for i in range(60):
            try:
                if driver.find_element_by_xpath("//strong[contains(.,'Customer added successfully')]").is_displayed(): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
        driver.find_element_by_xpath("//fieldset/div/div/div/div/span").click()
        # Select server to assign it to customer
        driver.find_element_by_link_text("FS-FSS-H5-140").click()
        driver.find_element_by_xpath("//label[contains(.,'Shared')]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[4]").click()
        # Select the Storage Pool
        driver.find_element_by_xpath("//span[contains(.,'StoragePool-1')]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        for i in range(60):
            try:
                if driver.find_element_by_xpath("//strong[contains(.,'Customer updated successfully')]").is_displayed(): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_xpath("//span[contains(.,'Manage')]").click()
	#Create SAN Resource
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
                if driver.find_element_by_xpath("//strong[contains(.,'The virtual device has been created.')]").is_displayed(): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_xpath("//div[@id='center']/div/div[2]/div[2]/div/div/div/div").click()
	#Create Snapshot Resource
        driver.find_element_by_xpath("//button[contains(@data-template-url,'views/manage/snapshot-menu.tpl.html')]").click()
        driver.find_element_by_link_text("Create Snapshot Resource").click()
	time.sleep(2)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        for i in range(60):
            try:
                if driver.find_element_by_xpath("//strong[contains(.,'Snapshot resource created successfully')]").is_displayed(): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        #driver.find_element_by_xpath("//div[@id='center']/div/div[2]/div[2]/div/div/div/div").click()
        #driver.find_element_by_xpath("//div[4]/button").click()
        #driver.find_element_by_link_text("Snapshot Resource").click()
        #driver.find_element_by_xpath("//li[7]/a/span").click()
        #for i in range(60):
        #    try:
        #        if driver.find_element_by_xpath("//button[@type='submit']").is_displayed(): break
        #    except: pass
        #    time.sleep(1)
        #else: self.fail("time out")
        #driver.find_element_by_xpath("//button[@type='submit']").click()
        #for i in range(60):
        #    try:
        #        if driver.find_element_by_xpath("//div[@id='center']/div/div[2]/div[2]/div/div/div/div").is_displayed(): break
        #    except: pass
        #    time.sleep(1)
        #else: self.fail("time out")
	driver.find_element_by_xpath("//div[@col='0']").click()
        # Delet SAN Resource.
    	driver.find_element_by_xpath("//button[contains(@data-template-url,'views/manage/delete-device.tpl.html')]").click()
	driver.find_element_by_xpath("//a[contains(.,'Delete')]").click()
        for i in range(60):
            try:
                if driver.find_element_by_xpath("//button[@type='submit']").is_displayed(): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
	time.sleep(2)
        driver.find_element_by_xpath("//input[@type='checkbox']").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
	for i in range(60):
            try:
                if driver.find_element_by_xpath("//strong[contains(.,'The virtual device has been deleted.')]").is_displayed(): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")

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
