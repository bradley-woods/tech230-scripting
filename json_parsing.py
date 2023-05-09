# JSON Parsing

import json
import os
import urllib.request

json1 = json.loads(open("C:/Users/bradl/PycharmProjects/tech_230/python_scripting/example.json").read())
value1 = json1['website']
print(value1)

# json2 = json.load(open("C:/Users/bradl/PycharmProjects/tech_230/python_scripting/example.json"))
# value2 = json2['country']
# print(value2)

# Script for creating absolute path to the JSON file
# script_dir = os.path.dirname(__file__) # __file__ = folder you are working in e.g. python_scripting
# print("The script is located at: " + script_dir)
# script_absolute_path = os.path.join(script_dir, "example.json") # join folder path to the filename
# print("The script path is: " + script_absolute_path)

# script to parse json
# json3 = json.loads(open(script_absolute_path).read())
# value3 = json3["name"]
# print(value3)

# loop through the keys and values in the JSON object
# for keys in json3:
#     value3 = json3[keys]
#     print("The key and value are ({}) = ({})".format(keys, value3))

# Parse JSON from a remote url
# with urllib.request.urlopen("http://jsonplaceholder.typicode.com/todos/1") as url:
#     data = json.load(url)
#     print(data)
    