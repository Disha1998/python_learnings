import requests
import json

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)
data = response.json()

with open('userData.json', 'w') as f:
    json.dump(data, f, indent=2) #without indent i get the data unstructured, and if you use indent=1 or 2 then it will be display in structure , took a reference from SMB
# print(data)





# def fetch_id_name_from_json():
#     with open('userData.json', 'r') as f:
#         data = json.load(f)
#         # print(data)
#         id = data.get('id')
#         name = data.get('name')
#         print(id, ": id", name , " : name")

#         # return id, name
# fetch_id_name_from_json()


def fetch_id_name_from_json():
    with open('userData.json', 'r') as f:
        data = json.load(f)
        id_and_name = []
        if len(data) > 0:
            for user in data:
              
                id = user.get('id')
                name = user.get('name')
                id_and_name.append(id)
                id_and_name.append(name)
                print(id_and_name)
                # print(id, ": id", name, " : name")
               
            with open('user_id_name.json', 'w') as f:
                     json.dump(id_and_name, f, indent=2)

# fetch_id_name_from_json()



#  next i can do is get the city from the address and there is lat, lang which is also a nested directry

def get_city():
     with open('userData.json', 'r') as f:
        data=  json.load(f)
        # print(data,'----')
      
        forCity = []
        for user in data:
              address = user.get('address')
              city = address.get('city')
            #   print(city)

              forCity.append(city)

        with open('user_city.json', 'w') as f:
                  json.dump(forCity, f, indent=2)
# get_city()


# get latitude and lang from geo

def get_lat_lng():
     with open('userData.json', 'r') as f:
          data = json.load(f)

          store_geo = []
          for geo in data:
              address = geo.get('address')
    #  print(address)
              get_geo = address.get('geo')
              print(get_geo)

              store_geo.append(get_geo)
            
          with open('all_lat_and_lang.json', 'w') as fi:
            json.dump(store_geo, fi, indent=2)
# get_lat_lng()



# let's get - username, phone num,  company name, city & zipcode


def get_details():
    with open('userData.json', 'r') as f:
        all_data = json.load(f)
        
        all_info = []
        for details in all_data:
            # user_name = details.get('username')
            # phon_num = details.get('phone')
            # company = details.get('company')
            # company_name = company.get('name')
            # address = details.get('address')
            # city = address.get('city')
            # zip = address.get('zipcode')
            
            # all_info.append(user_name)
            # all_info.append(phon_num)
            # all_info.append(company_name)
            # all_info.append(city)
            # all_info.append(zip)
            
             company_details = {
        "user_name": details.get('username'),
        "phone": details.get('phone'),
        "company": details.get('company').get('name'),
        "city": details.get('address').get('city'),
        "zipcode": details.get('address').get('zipcode')
    }
             
    
             all_info.append(company_details)
            
    print(all_info)
    with open('all_company_info.json', 'w') as f:
            json.dump(all_info, f, indent=2)
        
get_details()
            
            




