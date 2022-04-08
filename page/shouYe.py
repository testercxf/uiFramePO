#!/usr/bin/env python

from selenium import  webdriver
from selenium.webdriver.common.by import By
from base.base import WebDriver
import time as t

class shouYePage(WebDriver):
	firstPageNaviloc = (By.XPATH,'//div[@class="top"]/span')
	loginTextloc = (By.CSS_SELECTOR,'div.login>a:nth-child(1)')
	regisTextloc = (By.CSS_SELECTOR,'div.login>a:nth-child(3)')
	searchloc = (By.XPATH, '/html/body/div/div/div/div/form/input[1]')
	searchButtonloc = (By.XPATH, '/html/body/div/div/div/div/form/input[2]')
	searchContentloc = (By.XPATH, "//div[@class='nomsg']")
	myGouwucheloc = (By.XPATH,"//div[@class='small_cart_name']/span")



	@property
	def firstPageNavi(self):
		t.sleep(2)
		return self.findElement(*self.firstPageNaviloc).text

	@property
	def loginText(self):
		t.sleep(2)
		return self.findElement(*self.loginTextloc).text

	@property
	def regisText(self):
		t.sleep(2)
		return self.findElement(*self.regisTextloc).text


	def searchButton(self,inputData):
		t.sleep(2)
		self.findElement(*self.searchloc).send_keys(inputData)

	@property
	def searchButtonClick(self):
		self.findElement(*self.searchButtonloc).click()

	@property
	def searchContent(self):
		t.sleep(8)
		return self.findElement(*self.searchContentloc).text

	@property
	def myGouwucheClick(self):
		self.findElement(*self.myGouwucheloc).click()



