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

        if len(data) > 0:
            for user in data:
                id = user.get('id')
                name = user.get('name')
                print(id, ": id", name, " : name")
        else:
            print("No data found in the JSON file.")

# Call the function
fetch_id_name_from_json()


#  next i can do is get the city from the address and there is lat, lang which is also a nested directry

# store in json fille