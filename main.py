from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
import time
import xlsxwriter

workbook = xlsxwriter.Workbook("job_python.xlsx")
worksheet = workbook.add_worksheet()

browser = webdriver.Chrome()
browser.get("http://www.saramin.co.kr/zf_user/search/recruit?search_area=main&search_done=y&search_optional_item=n&searchType=search&searchword=python&recruitPage=1")
time.sleep(3)

soup = BeautifulSoup(browser.page_source,'html.parser')

df = pd.DataFrame(columns=['공고명','회사명','근무지역','채용조건'])

row_cnt = 1

for j in soup.findAll('div',class_='item_recruit'):
    job_name = j.find('h2',class_='job_tit').text.strip()
    company = j.find('strong',class_='corp_name').text
    working_area = j.find('div',class_='job_condition').find('a').text.strip()
    job_info = j.find('div',class_='job_condition')
    [s.extract() for s in job_info('a')]
    job_info = job_info.text.strip()
    df = df.append({'공고명':job_name,'회사명':company,'근무지역':working_area,'채용조건':job_info}, ignore_index = True)
    worksheet.write('A{}'.format(row_cnt),job_name)
    worksheet.write('B{}'.format(row_cnt),company)
    worksheet.write('C{}'.format(row_cnt),working_area)
    worksheet.write('D{}'.format(row_cnt),job_info)
    row_cnt += 1

for i in range(2,11):
    browser.find_element_by_xpath('//*[@id="recruit_info_list"]/div[2]/div/a[{}]'.format(i)).click()
    time.sleep(3)
    for i in soup.findAll('div',class_='item_recruit'):
        job_name = i.find('h2',class_='job_tit').text.strip()
        company = i.find('strong',class_='corp_name').text
        job_info = i.find('div',class_='job_condition').text.strip()
        df = df.append({'공고명':job_name,'회사명':company,'근무지역':working_area,'채용조건':job_info}, ignore_index = True)
        worksheet.write('A{}'.format(row_cnt),job_name)
        worksheet.write('B{}'.format(row_cnt),company)
        worksheet.write('C{}'.format(row_cnt),working_area)
        worksheet.write('D{}'.format(row_cnt),job_info)
        row_cnt += 1

for i in range(2,12):
    browser.find_element_by_xpath('//*[@id="recruit_info_list"]/div[2]/div/a[{}]'.format(i)).click()
    time.sleep(3)
    for i in soup.findAll('div',class_='item_recruit'):
        job_name = i.find('h2',class_='job_tit').text.strip()
        company = i.find('strong',class_='corp_name').text
        job_info = i.find('div',class_='job_condition').text.strip()
        df = df.append({'공고명':job_name,'회사명':company,'근무지역':working_area,'채용조건':job_info}, ignore_index = True)
        worksheet.write('A{}'.format(row_cnt),job_name)
        worksheet.write('B{}'.format(row_cnt),company)
        worksheet.write('C{}'.format(row_cnt),working_area)
        worksheet.write('D{}'.format(row_cnt),job_info)
        row_cnt += 1

for i in range(3,6):
    browser.find_element_by_xpath('//*[@id="recruit_info_list"]/div[2]/div/a[{}]'.format(i)).click()
    time.sleep(3)
    for i in soup.findAll('div',class_='item_recruit'):
        job_name = i.find('h2',class_='job_tit').text.strip()
        company = i.find('strong',class_='corp_name').text
        job_info = i.find('div',class_='job_condition').text.strip()
        df = df.append({'공고명':job_name,'회사명':company,'근무지역':working_area,'채용조건':job_info}, ignore_index = True)
        worksheet.write('A{}'.format(row_cnt),job_name)
        worksheet.write('B{}'.format(row_cnt),company)
        worksheet.write('C{}'.format(row_cnt),working_area)
        worksheet.write('D{}'.format(row_cnt),job_info)
        row_cnt += 1

browser.quit()

workbook.close()