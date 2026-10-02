import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
#Here is the code to make a GET request to the URL and store the response in a variable called 'response'.
response = requests.get(url)
print(response)

if response.status_code == 200:
    data_json = response.json()
    data_restaurants = {}
    for item in data_json:
        restaurant_name = item['Company']
        if restaurant_name not in data_restaurants:
            data_restaurants[restaurant_name] = []

        data_restaurants[restaurant_name].append({
            "item": item['Item'],
            "price": item['price'],
            "description": item['description'],
        })

else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")

for restaurant_name, data in data_restaurants.items():
    file_name = f"{restaurant_name}.json"
    with open(file_name, 'w') as file_restaurant:
        json.dump(data, file_restaurant, indent=4)