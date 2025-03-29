import json
import requests
url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)
data = response.json()

with open('post_data.json', 'w') as f:
     json.dump(data, f, indent=2)
# print(data)



# read the data from that json file

# with open('post_data.json', 'r') as f:
#     data= json.load(f)
# # name_and_id = []

# if len(data) > 0:
#     for items in data:     
#         id = items.get('userId')
#         title = items.get('title')
#     with open('post_id_title.json', 'w') as f:
#         json.dump(items, f, indent=2)
# print('read the data :: ', data)


def fetch_id_name_from_json():
    with open('post_data.json', 'r') as f:
        items = []
        data = json.load(f)   

        if len(data) > 0:  
            for user in data:  
                id = user.get('id')  
                title = user.get('title')  
                # print(id, ":-- id", title, " : --- title")
                items.append(id)
                items.append(title)

                with open('id_and_title_data.json', 'w') as f:
                    json.dump(items, f, indent=2)
   

fetch_id_name_from_json()