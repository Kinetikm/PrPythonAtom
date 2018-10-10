
import requests
import json

url = 'http://127.0.0.1:5000/get_classifier_result/'
headers = {'Content-type': 'application/json',
           'Accept': 'text/plain',
           'Content-Encoding': 'utf-8'}
predict_value_pool = ["ququ", "khdkjfhdkjfhdkjfhdf", "рпоарпоарпоарп", 12, 143., {"key":"value"}]
for i in predict_value_pool:
    data = {"predict" : i}
    answer = requests.post(url + "1", data=json.dumps(data), headers=headers)
    response = answer.json()
    assert answer.status_code == 200
    assert response['version'] == 1
    assert response['predict'] == i
    
    data = {"old_predict": i}
    answer = requests.post(url + "0", data=json.dumps(data), headers=headers)
    response = answer.json()
    assert answer.status_code == 200
    assert response['version'] == 0
    assert response['predict'] == i
print("Test ok")