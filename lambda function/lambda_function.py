import json


def build_response(meesgae):
    return {
        "sessionAttributes":{
           
        },
        "dialogAction":{
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
                "contentType": "PlainText",
                "content": meesgae
            }
        }
    }

def lambda_handler(event, context):
    
    result = 0
    
    numone_slot = event['currentIntent']['slots']['numone']
    numtwo_slot = event['currentIntent']['slots']['numtwo']
    
    numtwo_slot_parse_int = int(numtwo_slot)
    
    if 'addition' == event["currentIntent"]["name"]:
        result = int(numone_slot) + int(numtwo_slot)
        return build_response(result)
    elif 'subtraction' == event["currentIntent"]['name']:
        result = int(numone_slot) - int(numtwo_slot)
        return build_response(result)
    elif 'multiplication' == event["currentIntent"]['name']:
        result = int(numone_slot) * int(numtwo_slot)
        return build_response(result)
    elif 'division' == event["currentIntent"]['name']:
        if numtwo_slot_parse_int == 0 :
            return build_response('You Cant Divide By Zero')
        result = int(numone_slot) / int(numtwo_slot)
        return build_response(result)
   