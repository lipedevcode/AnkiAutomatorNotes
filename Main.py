import json
import urllib.request
import dados

def requestAddNote(action, **params):
    return {'action': action, 'params': params, 'version': 6}

def invoke(action, **params):
    requestJson = json.dumps(requestAddNote(action, **params)).encode('utf-8')
    response = json.load(urllib.request.urlopen(urllib.request.Request('http://127.0.0.1:8765', requestJson)))
    if len(response) != 2:
        raise Exception('response has an unexpected number of fields')
    if 'error' not in response:
        raise Exception('response is missing required error field')
    if 'result' not in response:
        raise Exception('response is missing required result field')
    if response['error'] is not None:
        raise Exception(response['error'])
    return response['result']
def main():
    api = dados.api
    for key in api.keys():
        invoke('addNote', note = {
                "deckName": "Inglês com Pedro Galvão",
                "modelName": "Basic",
                "fields": {
                    "Front": api[key]['frente'],
                    "Back": api[key]['verso']
                },
                "options": {
                    "allowDuplicate": True
                }
            })
if __name__ == '__main__':
    main()