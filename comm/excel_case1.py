# -*- coding: utf-8 -*-
import xlrd
import unittest
import requests
import json
import interface.readConfig as readConfig

localReadConfig = readConfig.ReadConfig()
workbook = None


class read_excle(unittest.TestCase):

    def open_excel(path):
        workbook = xlrd.open_workbook(r'F:\file_excel\sample.xlsx')



if __name__ == '__main__':
    unittest.main()
