#!/usr/bin/env python
import  unittest
import os
from utils import HTMLTestRunner
from utils.read_file import filePath
import  time


def getSuites():
	suites=unittest.defaultTestLoader.discover(
		start_dir=os.path.dirname(__file__),
		pattern='test_*.py',
		top_level_dir=None
	)
	print(os.path.dirname(__file__))
	return suites


def getNowTime():
	return time.strftime('%y-%m-%d-%H-%M-%S',time.localtime())


def run():
	filename=filePath('report',getNowTime()+'report.html')
	runner=HTMLTestRunner.HTMLTestRunner(
		stream=open(filename,'wb'),
		verbosity=2,
		title='自动化测试报告',
		description='自动化测试详细的报告'
	).run(getSuites())

if __name__ == '__main__':
    run()


