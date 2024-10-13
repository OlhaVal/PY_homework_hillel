import requests
url = 'http://127.0.0.1:8080'

filename = 'image.png'
files = {'image': open(filename, 'rb')}
upload_response = requests.post(f'{url}/upload', files=files)

if upload_response.status_code == 201:
    print("Відповідь запиту POST:", upload_response.json())
else:
    print(f"Помилка при запиті POST: {upload_response.status_code} - {upload_response.text}")

get_response = requests.get(f'{url}/image/{filename}', headers={'Content-Type': 'text'})

if get_response.status_code == 200:
    print("Відповідь запиту GET:", get_response.json())
else:
    print(f"Помилка при запиті GET: {get_response.status_code} - {get_response.text}")

delete_response = requests.delete(f'{url}/delete/{filename}')

if delete_response.status_code == 200:
    print("Відповідь запиту DELETE:", delete_response.json())
else:
    print(f"Помилка при запиті DELETE: {delete_response.status_code} - {delete_response.text}")