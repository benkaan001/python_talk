import json

people_string = '''
{
    "people": [
        {
            "name": "John Smith",
            "phone": "123-456-9999",
            "emails": ["john@test.com","jsmith@test.com"],
            "has_license": false
        },
        {
            "name": "Jane Doe",
            "phone": "123-555-1111",
            "emails": null,
            "has_license": true
        }
        
    ]
}

'''

data = json.loads(people_string)

print(type(data))  # <class 'dict'>

for person in data['people']:
    print(person)
"""
{'name': 'John Smith', 'phone': '123-456-9999', 'emails': ['john@test.com', 'jsmith@test.com'], 'has_license': False}
{'name': 'Jane Doe', 'phone': '123-555-1111', 'emails': None, 'has_license': True}
"""
for person in data['people']:
    print(person['name'],end=" ") # John Smith Jane Doe
    
# remove the phone numbers from each person
for person in data['people']:
    del person['phone']

# dump back the python object into a string
new_string = json.dumps(data)
print(new_string)
# {"people": [{"name": "John Smith", "emails": ["john@test.com", "jsmith@test.com"], "has_license": false}, {"name": "Jane Doe", "emails": null, "has_license": true}]}

# add indentation 
new_string = json.dumps(data, indent=2)
print(new_string)
"""
{
  "people": [
    {
      "name": "John Smith",
      "emails": [
        "john@test.com",
        "jsmith@test.com"
      ],
      "has_license": false
    },
    {
      "name": "Jane Doe",
      "emails": null,
      "has_license": true
    }
  ]
}

"""

# sort keys in alphabetical order
new_string = json.dumps(data, indent=2, sort_keys=True)
print(new_string)
"""
{
  "people": [
    {
      "emails": [
        "john@test.com",
        "jsmith@test.com"
      ],
      "has_license": false,
      "name": "John Smith"
    },
    {
      "emails": null,
      "has_license": true,
      "name": "Jane Doe"
    }
  ]
}

"""

