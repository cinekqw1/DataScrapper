

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome('/Users/marcin/PycharmProjects/data_s_1/driver/chromedriver');


browser.get("https://www.skyscanner.net/transport/flights/waw/pra/191218/200219/?adults=1&children=0&adultsv2=1&childrenv2=&infants=0&cabinclass=economy&rtn=1&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false&ref=home#results")



prices = [price.text for price in wait(browser, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "price")))]
print(prices)