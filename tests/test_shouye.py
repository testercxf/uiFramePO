#!/usr/bin/env python

import  unittest
from page.shouYe import shouYePage
from page.login import LoginPage
from base.base import Base

class Shouye(unittest.TestCase):


	def setUp(self):
		self.driver = Base().initWebDriver("A")


	def testshouye01_01(self):
		'''验证首页导航栏文案显示是否正常'''
		LoginPage(self.driver).login("17778917187","123qwe")
		m = shouYePage(self.driver)
		self.assertEqual(m.firstPageNavi,"亲，欢迎您来到云商系统商城！")
		self.assertEqual(m.loginText, "17778917187")
		self.assertEqual(m.regisText, "退出")


	def testshouye01_02(self):
		'''验证搜索功能'''
		LoginPage(self.driver).login("17778917187","123qwe")
		m = shouYePage(self.driver)
		m.searchButton("王麻子")
		m.searchButtonClick
		self.assertEqual(m.searchContent,"抱歉，没有找到相关的商品")


	def tearDown(self):
		self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
