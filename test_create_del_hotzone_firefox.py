# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestCreateDelHotZoneFirefox(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(command_executor='http://172.17.0.3:4444/wd/hub',desired_capabilities=DesiredCapabilities.FIREFOX)
        self.driver.implicitly_wait(30)
        self.base_url = "http://172.17.0.2/"
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_create_del_hotzone_firefox(self):
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
        driver.find_element_by_xpath("//span[contains(.,'Customers')]").click()
	driver.find_element_by_xpath("//button[@type='button']").click()
        driver.find_element_by_xpath("(//input[@type='text'])[2]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys("test")
        driver.find_element_by_xpath("(//input[@type='text'])[3]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[3]").send_keys("test.com")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        for i in range(60):
            try:
                if driver.find_element_by_xpath("//strong[contains(.,'The customer has been added.')]").is_displayed(): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_xpath("//button[contains(@ng-click,'showAssignDialog(customerGrid.selectedRows[0])')]").click()
	time.sleep(1)
	# Select server to assign it to customer
	driver.find_element_by_xpath("//span[@aria-label='Select box activate']").click()
        driver.find_element_by_link_text("FS-FSS-H5-140").click()
        driver.find_element_by_xpath("//label[contains(.,'Shared')]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[4]").click()
        # Select the Storage Pool
        driver.find_element_by_xpath("//span[contains(.,'StoragePool-1')]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        for i in range(60):
            try:
                if driver.find_element_by_xpath("//strong[contains(.,'The customer has been updated.')]").is_displayed(): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_xpath("//span[contains(.,'Manage')]").click()
        # Create a Virtual Device
        driver.find_element_by_xpath("//button[contains(@ng-click,'showCreateVirtualDeviceDialog(currentDevice)')]").click()
        driver.find_element_by_name("totalSize").clear()
        driver.find_element_by_name("totalSize").send_keys("1024")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        for i in range(60):
            try:
                if driver.find_element_by_xpath("//strong[contains(.,'The virtual device has been created.')]").is_displayed(): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
	driver.find_element_by_xpath("//div[@col='0']").click()
        # Create HotZone
        driver.find_element_by_xpath("//button[contains(@data-template-url,'views/manage/hotzone-menu.tpl.html')]").click()
	driver.find_element_by_xpath("//a[contains(.,'Create HotZone')]").click()
        for i in range(60):
            try:
                if driver.find_element_by_xpath("//button[contains(.,'Create')]").is_displayed(): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
	time.sleep(1)
	driver.find_element_by_xpath("//span[@ng-show='$select.isEmpty()']").click()
        driver.find_element_by_xpath("//span[contains(.,'StoragePool-1')]").click()
	driver.find_element_by_xpath("//button[@type='submit']").click()
        for i in range(60):
            try:
                if driver.find_element_by_xpath("//strong[contains(.,'The HotZone has been created.')]").is_displayed(): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
	driver.find_element_by_xpath("//div[@col='0']").click()
        # Disable HotZone
	driver.find_element_by_xpath("//button[contains(@data-template-url,'views/manage/hotzone-menu.tpl.html')]").click()
	for i in range(60):
            try:
                if driver.find_element_by_xpath("//a[contains(.,'Delete HotZone')]").is_displayed(): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
	driver.find_element_by_xpath("//a[contains(.,'Delete HotZone')]").click()
        driver.find_element_by_xpath("//button[contains(.,'Delete')]").click()
        for i in range(60):
            try:
                if driver.find_element_by_xpath("//strong[contains(.,'The HotZone has been deleted.')]").is_displayed(): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_xpath("//div[@col='0']").click()
	# Delete Virtual Device
        driver.find_element_by_xpath("//button[contains(@data-template-url,'views/manage/delete-device.tpl.html')]").click()
	driver.find_element_by_xpath("//a[contains(.,'Delete')]").click()
        for i in range(60):
            try:
                if driver.find_element_by_xpath("//button[@type='submit']").is_displayed(): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_xpath("//input[@type='checkbox']").click()
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
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
    #unittest.main()
