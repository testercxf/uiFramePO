#!/usr/bin/env python

import  unittest
from page.shouYe import shouYePage
from page.gouwuChe import buyCarDetailPage
from page.login import LoginPage
from base.base import Base

class Gouwuche(unittest.TestCase):

	def setUp(self):
		self.driver = Base().initWebDriver("A")

	def testshouye01_03(self):
		LoginPage(self.driver).login("17778917187","123qwe")
		mGouwuche = shouYePage(self.driver)
		mGouwucheDetail = buyCarDetailPage(self.driver)
		mGouwuche.myGouwucheClick
		self.assertEqual("购物车内暂时没有商品",mGouwucheDetail.CarDetailTitle)

	def tearDown(self):
		self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
