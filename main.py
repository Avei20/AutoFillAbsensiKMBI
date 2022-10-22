import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime

status = input('WFH/WFO? ')

DRIVER_PATH = './webdriver/geckodriver-linux'
driver = webdriver.Firefox(executable_path = DRIVER_PATH)
print(os.path.join('./webdriver/geckodriver-win.exe'))

url = 'https://forms.gle/NXixKVX3uYfwQ4wm6'

driver.get(url)

nip = '2205066'
nama_lengkap = 'Muhammad Abdul Aziz Al-Ghofari'
universitas = ''

nip_input = driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
nip_input.click()
nip_input.send_keys(nip)

nama_input = driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
nama_input.click()
nama_input.send_keys(nama_lengkap)

nim = '2301932153'
nim_input = driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
nim_input.send_keys(nim)

open_univ_list = driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]')
open_univ_list.click()

universitas_input = driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[2]/div[8]/span')
universitas_input.click()

open_satker_list = driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[2]')
open_satker_list.click()

satker_input = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[2]/div[3]/span')
satker_input.click()

current = datetime.now()

year = current.year
month = current.month
day = current.day

day_input = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div/div[1]/input')
day_input.send_keys(day)

month_input = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[3]/div/div[2]/div[1]/div/div[1]/input')
month_input.send_keys(month)

year_input = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[5]/div/div[2]/div[1]/div/div[1]/input')
year_input.send_keys(year)

open_angkatan_llist = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div[2]')
open_angkatan_llist.click()
angkatan_input = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[2]/div[3]/span')
angkatan_input.click()

next_btm_page1 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span')
next_btm_page1.click()

time.sleep(2)

wfh_radio = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div')
wfo_radio = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div')

if (status == 'WFH' or status == 'h' or status == 'H' or status=='wfh') :
    wfh_radio.click()
elif (status == 'WFO' or status =='O' or status =='o' or status == 'wfo') : 
    wfo_radio.click()

next_btn_page2 = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
next_btn_page2.click()

buddy = 'Intan Pratiwi'

buddy_input = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
buddy_input.click()
buddy_input.send_keys(buddy)

submit_btn = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
# submit_btn.click()