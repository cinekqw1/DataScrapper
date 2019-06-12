from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

city_from = "war"
city_dest = "pra"
adults = 1
children = 2


browser = webdriver.Chrome('/Users/marcin/PycharmProjects/data_s_1/driver/chromedriver');
url = "https://www.skyscanner.net/transport/flights/"+city_from+"/"+city_dest+"/191218/200219/?adults="+str(adults)+"&children="+str(children)+"&adultsv2=1&childrenv2=&infants=0&cabinclass=economy&rtn=1&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false&ref=home#results"
browser.get(url)
prices = [price.text for price in wait(browser, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "price")))]
print(prices)


