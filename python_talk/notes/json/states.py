import json

with open('states.json') as f:
    data = json.load(f)

for state in data['states']:
    print(state)
'''
{'name': 'Alabama', 'abbreviation': 'AL'}
{'name': 'Alaska', 'abbreviation': 'AK'}
'''

for state in data['states']:
    if state['abbreviation'].startswith("A"):
        print(state['name'].upper(), state['abbreviation'].lower())
    """
    ALABAMA al
    ALASKA ak
    AMERICAN SAMOA as
    ARIZONA az
    ARKANSAS ar
    """
    
# transform the data before writing it back to a new JSON file
for state in data['states']:
    del state['abbreviation']

with open('just_states.json', 'w') as f:
    json.dump(data, f, indent=2)