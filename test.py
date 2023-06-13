import requests

# response = requests.post('http://127.0.0.1:5000/announcement',
#                          json={'title':'title3',
#                                'description': 'qweqwe',
#                                'owner': 'owner1'})

# response = requests.get('http://127.0.0.1:5000/announcement/2')

response = requests.delete('http://127.0.0.1:5000/announcement/1')

print(response.json())