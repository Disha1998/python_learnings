import requests
from bs4 import BeautifulSoup
import pandas as pd
import json


title_list = []
price_list=[]
desc_list = []
reviews_list = []

url = "https://www.airbnb.co.in/s/homes?dynamic_product_ids%5B%5D=21916374&omni_page_id=36021&refinements%5B%5D%5B0%5D=vacation-rentals"

r = requests.get(url)
# print(r)

soup = BeautifulSoup(r.text,"html.parser")

try:
    while True:
        
        title = soup.find_all("div", {"class":"t1jojoys"})
        # print(title)
        for i in title:
            name = i.text
            # print(name)
            title_list.append(name)
        # print(title_list)
        
        price = soup.find_all('span', {"class" : "_1qgfaxb1"})
        for i in price:
            p = i.text
            # print(p, '---price')
            price_list.append(p)
        # print(price_list)
        
        description = soup.find_all("span", {"data-testid" : "listing-card-name"})
        for i in description:
            desc = i.text
            desc_list.append(desc)
        # print(desc_list)
        
        reviews = soup.find_all("div", {"class" : "t1a9j9y7 atm_da_1ko3t4y atm_dm_kb7nvz atm_fg_h9n0ih dir dir-ltr"})
        for i in reviews:
            revw = i.text
            reviews_list.append(revw)
        # print(reviews_list)
    
    # print(soup)


        allUrl = []
        allUrl.append(url)
        while True:
         next_page = soup.find("a", {"aria-label" : "Next"}).get("href")
         complete_new_page = "https://www.airbnb.co.in"+ next_page
        # print(complete_new_page,':: next page')
         allUrl.append(complete_new_page)
    
    # this is for go in to the next page, so wht it does, it 

         url = complete_new_page
         r=requests.get(url)
         soup = BeautifulSoup(r.text,"html.parser")
        
         with open("Airbnb_Delhi/all_page_urls.json", 'w') as f:
                json.dump(allUrl, f, indent=4)

except: pass

full_data={
    'title' : title_list,
    'description' : desc_list,
    'review' : reviews_list,
    "price" : price_list
}

with open("Airbnb_Delhi/airbnb_gandhinagar.json", 'w') as f:
    json.dump(full_data, f, indent=2)
    
# data_frame = pd.DataFrame({
#     'title' : title_list,
#     'description' : desc_list,
#     'review' : reviews_list,
#     "price" : price_list
#     })
    
# data_frame.to_csv("airbnb_gandhinagar.csv")