

from bs4 import BeautifulSoup as soup

import time
import pandas as pd

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path = 'C://Users//yz14091//Documents//chromedriver')
driver.set_window_size(1400,1000)

my_url= "https://pmt-eu.hosted.exlibrisgroup.com/primo-explore/search?query=any,contains,%22energy%20system%22%20OR%20%22energy%20sector%22%20OR%20%22energy%20industry%22,AND&query=any,contains,%22skills%20gap%22%20OR%20%22skills%20mismatch%22%20OR%20%22skills%20shortage%22%20OR%20%22skills%20needs%22%20OR%20%22skills%20requirements%22,AND&query=any,contains,model,AND&query=any,contains,jobs,AND&pfilter=lang,exact,eng,AND&tab=default_tab&search_scope=default_scope&sortby=rank&vid=44BU_VU1&lang=en_US&mode=advanced&offset=0"
driver.get(my_url)
#wait = ui.WebDriverWait(driver,20)

citation_list = []	 

first_result_xpath = '//*[@id="SEARCH_RESULT_RECORDID_TN_oecd_s10_1787_5jz123fgkxjl_en"]/div[3]/prm-brief-result'
wait_1 = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,first_result_xpath)))
first_result_btn = driver.find_element_by_xpath(first_result_xpath).click()


next_result_xpath = '//*[@id="primoExploreRoot"]/body/primo-explore/div[3]/div/button[2]/prm-icon/md-icon'

wait_next = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,next_result_xpath)))
time.sleep(3)
next_result_btn = driver.find_element_by_xpath(next_result_xpath).click()



next_result_xpath = '//*[@id="primoExploreRoot"]/body/primo-explore/div[3]/div/button[3]/prm-icon/md-icon'

for nn in list(range(1,300)):
	wait_next = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,next_result_xpath)))
	time.sleep(3)
	next_result_btn = driver.find_element_by_xpath(next_result_xpath).click()

while True:
	try:

		wait_next = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,next_result_xpath)))
		time.sleep(3)
		next_result_btn = driver.find_element_by_xpath(next_result_xpath).click()

		#next_result_btn = driver.find_element_by_xpath(next_result_xpath).click()
		cite_xpath = '//*[@id="Citation"]/button/span/div/prm-icon/md-icon'
		wait_cite = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,cite_xpath)))
		cite_btn = driver.find_element_by_xpath(cite_xpath).click()

		wait_copy_cite = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="copy-citation-button"]/span')))
		page = driver.page_source
		page_soup = soup(page,"html.parser")
		citation = page_soup.find("div",{"class": "form-focus layout-padding layout-align-center-center layout-row"})
		print(citation.get_text())
		citation_list.append(citation.get_text())
	except:
		print('End of search results')


refs = pd.DataFrame(citation_list).to_csv('C://Users//yz14091//Documents//refs.csv')


