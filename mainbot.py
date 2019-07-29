# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import sys

# own module
import model
import crud
import scraper
import logger
from config import * 

class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        options = Options()
        options.add_argument("--headless")


        self.driver = webdriver.Firefox(options=options)
        # self.driver.implicitly_wait(30)
        # self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_app_dynamics_job(self):
        driver = self.driver
        # login
        driver.get("https://mbasic.facebook.com/")
        driver.find_element_by_id("m_login_email").click()
        driver.find_element_by_id("m_login_email").clear()
        driver.find_element_by_id("m_login_email").send_keys(FBusername)
        # x = driver.find_element_by_id("m_login_email").innerHTML();
        # print x
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(FBpassword)
        x = driver.find_element_by_name("pass").get_attribute("value")
        driver.find_element_by_name("login").click()
        driver.find_element_by_link_text("Not Now").click()

        # ngepost
        driver.get(page_url)
        driver.find_element_by_id("u_0_0").click()
        driver.find_element_by_id("u_0_0").clear()
        driver.find_element_by_id("u_0_0").send_keys(post)
        driver.find_element_by_name("view_post").click()
        
        # close browser fix
        driver.quit()


    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
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
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)

def analize():
    return 0

def debug():
    return 0

def initialize_post():
    event = crud.getEventBelumPosting()
    global post
    if(event == None):
        return 1
    else:
        post = text_post_parser(event)
        # update post done
        crud.updateDone(event)

    return 0

def text_post_parser(event):
    
    post_text = """
Judul : {}

Link : {}

Waktu : {}
"""
    
    post_text = post_text.format(event.judul.encode('utf8'), event.link.encode('utf8'), event.waktu_event) 
    post_text = post_text.strip()
    return post_text

def crawl():
    newUpdate = scraper.checkWebUpdate()
    if(newUpdate == 1):
        logger.printlogstat("New Update : On Web")        
    elif(newUpdate == 0):
        logger.printlogstat("No update")        

    return 0

# global variable
post = "Payung Teduh"
if __name__ == "__main__":
    logger.start()
    analize()
    debug()
    crawl()
    ret = initialize_post()
    if(ret == 0):
        unittest.main()
    logger.finish()