#!/usr/bin/env python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium import  webdriver
import time,os

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class Base(object):

	def initAPPDriver(self):
		desired_caps = {}
		self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
		time.sleep(45)
		return self.driver

	def initWebDriver(self,projectName):
		self.driver = webdriver.Chrome()
		if projectName == "A":
			self.driver.get("http://101.133.169.100/yuns/index.php")
		elif projectName == "B":
			self.driver.get("http://www.bcbxhome.com")
		self.driver.maximize_window()
		time.sleep(5)
		return self.driver


class WebDriver:
	def __init__(self,driver):
		self.driver=driver

	def __str__(self):
		return 'driver'

	def findElement(self,*loc):
		try:
			return WebDriverWait(
				driver=self.driver,
				timeout=10).until(lambda x:x.find_element(*loc))
		except NoSuchElementException as e:
			return e.args[0]

	def findElements(self,*loc):
		try:
			return WebDriverWait(
				driver=self.driver,
				timeout=10).until(lambda x: x.find_elements(*loc))
		except NoSuchElementException as e:
			raise e.args[0]


class WebUi(WebDriver):
	def __str__(self):
		return 'web'

class AppUi(WebDriver):
	def __str__(self):
		return 'app'

