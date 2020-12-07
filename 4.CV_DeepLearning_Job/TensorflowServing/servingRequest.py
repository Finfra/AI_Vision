import json
import numpy
import requests
data = json.dumps({"signature_name": "serving_default",
                   "instances": [[2., 1., 3., 2.]] })
headers = {"content-type": "application/json"}
json_response = requests.post('http://s1:9001/v1/models/iris:predict',data=data, headers=headers)
#print(json_response) # 200 Success , 400 Fail
predictions = numpy.array(json.loads(json_response.text)["predictions"])
print(predictions)
