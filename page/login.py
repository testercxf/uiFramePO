#!/usr/bin/env python

from selenium import  webdriver
from selenium.webdriver.common.by import By
from base.base import WebDriver
import time as t

class LoginPage(WebDriver):
	loginEnterButton = (By.LINK_TEXT,'登录')
	username_loc=(By.NAME,'username')
	password_loc=(By.ID,'password')
	login_loc=(By.CLASS_NAME,'submit_login')


	@property
	def loginEnterButtonClick(self):
		t.sleep(1)
		return self.findElement(*self.loginEnterButton).click()

	def username(self,name):
		self.findElement(*self.username_loc).send_keys(name)

	def password(self,password):
		self.findElement(*self.password_loc).send_keys(password)

	@property
	def clickLogin(self):
		self.findElement(*self.login_loc).click()

	def login(self,name,passwd):
		self.loginEnterButtonClick
		self.username(name)
		self.password(passwd)
		self.clickLogin
		t.sleep(5)




