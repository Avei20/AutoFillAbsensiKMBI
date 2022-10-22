from selenium import webdriver
import os
from selenium.webdriver.common import keys

driver = webdriver.Firefox('./webdriver/geckodriver-linux')
print(os.path.join('./webdriver/geckodriver-win.exe'))

url = 'https://forms.gle/NXixKVX3uYfwQ4wm6'

# driver.get(url)

