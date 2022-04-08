#!/usr/bin/env python

from selenium.webdriver.common.by import By
from base.base import WebUi
import time as t

class buyCarDetailPage(WebUi):
	mygouwuCheloc = (By.XPATH,'//div[@class="r"]/span')


	@property
	def CarDetailTitle(self):
		t.sleep(4)
		return self.findElement(*self.mygouwuCheloc).text