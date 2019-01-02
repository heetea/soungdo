import time
from selenium import webdriver
import xlrd
from xlutils.copy import copy
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException
import os

results = []
# driver
driver = webdriver.Chrome(executable_path="/Users/heetae/desktop/chromedriver/chromedriver")

for i in range(1,321):
    driver.get("http://www.pharmon.co.kr/?c=information")

# 엑셀 파일 열기
    wb = xlrd.open_workbook('/Users/heetae/Downloads/2500.xlsx')
    sheet = wb.sheet_by_index(0)
# 검색 키워드 셀에서 가져오기
    song = sheet.cell(i, 1).value
    keyword = str(song) #숫자인 경우가 있어서 str()

    driver.implicitly_wait(1)

    try :
        elem = driver.find_element_by_name("code") 
        elem.send_keys(keyword)
        elem.submit()
        driver.implicitly_wait(5)
        medisonName = driver.find_element_by_id('rji06').text 
        results.append(medisonName)
    except NoSuchElementException:
        print(" [예외 발생] 표 없음 ")
        results.append("")
        continue
import pandas as pd

dataframe = pd.DataFrame(results)

    dataframe.to_csv("/Users/heetae/desktop/chromedriver/ab.csv", header=False, index =False)