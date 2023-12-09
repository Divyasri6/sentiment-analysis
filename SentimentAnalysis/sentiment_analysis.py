import requests
import json
def sentiment_analyzer(text_to_analyse):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    if response.status_code == 200:
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    elif response.status_code == 500:
        label = None
        score = None
    return {'label': label, 'score': score}

'''python3.11
   from sentiment_analysis import sentiment_analyzer
   sentiment_analyzer("I love this new technology")'''

'''import json
   from sentiment_analysis import sentiment_analyzer
    response = sentiment_analyzer("I love this new technology")
    formatted_response = json.loads(response)
    print(formatted_response)
    
    label = formatted_response['documentSentiment']['label']
    score = formatted_response['documentSentiment']['score']
>>> label
'SENT_POSITIVE'
>>> score
0.996954'''