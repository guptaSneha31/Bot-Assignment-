import json
def get_utterance_indices(utterance):
    utterance += " "
    index = 0
    for i in range(len(utterance)):
        if utterance[i] == ' ':
            print(utterance[index:i]+" "+str(index))
            index = i+1
    print("Last index : {}".format(len(utterance)-1))
with open('result.json') as json_file:
    data = json.load(json_file)
    #print(data['rasa_nlu_data']['common_examples']) #you have your dictinary here
    for item in data['rasa_nlu_data']['common_examples']:
        print("Utterance : {}".format(item['text']))
        print("Intent : {}".format(item['intent']))
        get_utterance_indices(item['text'])
        temp = input("enter first and last index and inent seperated by comma :").split(',')
        try:
            first,last,entity = temp[0],temp[1],temp[2]
            item['entities'].append({
                'start':first,
                'end':last,
                'value':item['text'][int(first):int(last)],
                'entity':entity
            })
            print("=======xxx=======xxx=======xxx==========xxx==========xxx\n\n\n")
        except:
            print("continuing=====xxx========xxx==========xxx=========\n\n\n")
            continue
with open('final_result.json', 'w') as fp:
    json.dump(data, fp,indent=4)