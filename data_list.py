import requests
import json
from bs4 import BeautifulSoup
import csv

url = "https://shop.qoin.world/"

i = 0

while i<=753:

    querystring = {"mylisting-ajax":"1","action":"get_listings","security":"a4d1c4714c","form_data[page]": str(i),"form_data[preserve_page]":"true","form_data[search_keywords]":"","form_data[category]":"","form_data[search_location]":"","form_data[lat]":"false","form_data[lng]":"false","form_data[proximity]":"20","form_data[tags]":"","form_data[sort]":"nearby","listing_type":"place","listing_wrap":"col-xs-6 grid-item"}

    headers = {
        'sec-ch-ua': "\" Not;A Brand\";v=\"99\", \"Google Chrome\";v=\"91\", \"Chromium\";v=\"91\"",
        'accept': "application/json, text/javascript, */*; q=0.01",
        'x-requested-with': "XMLHttpRequest",
        'sec-ch-ua-mobile': "?0",
        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36",
        'sec-fetch-site': "same-origin",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'cache-control': "no-cache",
        'postman-token': "d7057963-b566-9241-bfd7-5439ac2ac9b1"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = json.loads(response.text)

    if 'html' in data:
        response_html = data['html']

        response_html = BeautifulSoup(str(response_html), 'html.parser')

        divs = response_html.find_all('div',{'class':'col-xs-6'})

        for div in divs:
            business_name = ''
            email = ''
            phone = ''
            link = ''
            contact_person = ''
            address = ''

            try:
                a_tag = div.find('a')
                link = a_tag.get('href')

            except:
                print ("eror")

            try:
                business = div.find('h4')
                business_name = business.text.strip()

            except:
                print ("eror")

            try:
                ul = div.find('ul',{'class':'lf-contact'})
                lis = ul.find_all('li')

                for li in lis:
                    li_str = str(li)

                    if 'icon-phone-outgoing' in li_str:
                        if phone == '':
                            phone = li.text.strip()

                    if 'icon-location-pin-add-2' in li_str:
                        if address == '':
                            address = li.text.strip()



            except:
                print ("eror")



            temp = []
            temp.append(business_name)
            temp.append(phone)
            temp.append(link)
            temp.append(address)

            print (temp)

            arr = []
            arr.append(temp)

            with open('ipo_1.csv', 'a+') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerows(arr)


    i = i + 1