
import requests
import dotenv
import os
import datetime

dotenv.load_dotenv()

# Create User Profile

# parameters = {
#     'token': os.getenv('Pixela_token'),
#     'username': os.getenv('Pixela_user_name'),
#     'agreeTermsOfService':'yes',
#     'notMinor':'yes',
# }
#
# response = requests.post(url='https://pixe.la/v1/users', json=parameters)
#


#Create a Graph
pixela_endpoint = 'https://pixe.la/'
graph_endpoint = pixela_endpoint + f'/v1/users/{os.getenv('Pixela_user_name')}/graphs'

#print(graph_endpoint)

graph_config ={
    'id':'graph1',
    'name':'Daily Coding Tracker',
    'unit':'hour',
    'type':'float',
    'color':'shibafu',
    'timezone': 'America/Los_Angeles',
}

header = {'X-USER-TOKEN':f'{os.getenv('Pixela_token')}'}

# response = requests.post(url=graph_endpoint,json= graph_config, headers=header)
# print(response.text)

#Create a pixel
pixela_endpoint = 'https://pixe.la/'
graph_id = graph_config['id']
add_pixel_endpoint = pixela_endpoint + f'v1/users/{os.getenv('Pixela_user_name')}/graphs/{graph_id}'

print(add_pixel_endpoint)

date=datetime.datetime.now().date().strftime('%Y%m%d')


add_pixel_config = {
    'date':date,
    'quantity':'3.55',
}

response = requests.post(url=add_pixel_endpoint,headers=header,json=add_pixel_config)
print(response.text)




