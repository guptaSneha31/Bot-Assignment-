def  get_dict(text,intent=""):
    return {'text':text , 'intent':intent,'entities':[]}
filee = open('utterances.txt','r')
d={
  "rasa_nlu_data": {
    "regex_features": [
      {
        "name": "zipcode",
        "pattern": "[0-9]{5}"
      },
      {
        "name": "greet",
        "pattern": "hey[^\\s]*"
      }
    ],
    "entity_synonyms": [
      {
        "value": "chinese",
        "synonyms": ["Chinese", "Chines", "chines"]
      },
      {
        "value": "vegetarian",
        "synonyms": ["veggie", "vegg"]
      }
    ],
    "common_examples": []
  }
  }
used_intents = []
for line in filee.readlines():
    print("Input intent for :")
    print(line)
    print("used intents :")
    print(used_intents)
    intent = input("Intent :")
    if intent not in used_intents:
        used_intents.append(intent)
    d['rasa_nlu_data']['common_examples'].append(get_dict(line[:-1],intent))
import json
with open('result.json', 'w') as fp:
    json.dump(d, fp,indent=4)