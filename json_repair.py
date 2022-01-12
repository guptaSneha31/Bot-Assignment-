import json
def get_utterance_indices(utterance):
    utterance += " "
    index = 0
    for i in range(len(utterance)):
        if utterance[i] == ' ':
            print(utterance[index:i]+" "+str(index))
            index = i+1
    print("Last index : {}".format(len(utterance)-1))
with open('final_result.json') as json_file:
    data = json.load(json_file)
    #print(data['rasa_nlu_data']['common_examples']) #you have your dictinary here
    for item in data['rasa_nlu_data']['common_examples']:
        #print("Utterance : {}".format(item['text']))
        #print("Intent : {}".format(item['intent']))
        print(item)
        if len(item['entities'])>0:
            item['entities'][0]['start']  = int (item['entities'][0]['start'] )
            item['entities'][0]['end'] = int(item['entities'][0]['end'])
        
with open('final_result2.json', 'w') as fp:
    json.dump(data, fp,indent=4)