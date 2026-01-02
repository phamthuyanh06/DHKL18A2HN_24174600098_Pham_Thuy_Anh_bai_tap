import json

data = {
    "name": "G Văn A",
    "age": 23,
    "skills": ["AI", "Python"]
}

json_str = json.dumps(data)

print(json_str)
