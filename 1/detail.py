import requests
import json
from bs4 import BeautifulSoup
import csv

import requests
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument(
#     '--user-agent="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166"')
# chrome_options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome(options=chrome_options,
                          executable_path=ChromeDriverManager().install())

with open('1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print (row[2])

        url = row[2]

        driver.get(url)
        html2 = driver.page_source
        html = BeautifulSoup(html2, "lxml", from_encoding="utf-8")
        scripts = html.find('script',{'type':'application/ld+json'})

        scripts = str(scripts)
        scripts = scripts.replace('<script type="application/ld+json">','')
        scripts = scripts.replace('</script>','')

        data = json.loads(scripts)

        email = ''

        if 'email' in data:
            email = data['email']

            print (email)

        row.append(email)

        print (row)

        arr = []
        arr.append(row)

        with open('ipo_1_2.csv', 'a+') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(arr)