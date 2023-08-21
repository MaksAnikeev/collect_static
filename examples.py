import requests
from datetime import datetime
from pprint import pprint

# '''Создаем дату со статистикой'''
# url = 'http://127.0.0.1:8000/statistic_day/add'
# payload = {
#     'date': '2023-08-15',
#     'clicks': 81,
#     'views': 1200,
#     'cost': 179.68
# }
# response = requests.post(url, data=payload)
# response.raise_for_status()
# print(response.json())


'''Получаем данные по датам с выбором поля для упорядочивания вывода'''
url = 'http://127.0.0.1:8000/statistics/get'
payload = {
    'date_from': '2023-07-01',
    'date_to': '2023-08-21',
    'order': 'clicks'
}
response = requests.post(url, data=payload)
response.raise_for_status()
pprint(response.json())

# '''Очищаем статистику'''
# url = 'http://127.0.0.1:8000/statistics/clear'
# payload = {
#     'date_from': '2023-08-19',
#     'date_to': '2023-08-21',
#     'clear_all': None
# }
# response = requests.post(url, data=payload)
# response.raise_for_status()
# pprint(response.json())