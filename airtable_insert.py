import requests
import json

def insert_airtable_record(api_key, base_id, table_name, fields):
    headers = {
        'Authorization': 'Bearer ' + api_key,
        'Content-Type': 'application/json'
    }
    data = {
        'fields': fields
    }
    url = f'https://api.airtable.com/v0/{base_id}/{table_name}'
    response = requests.post(url, headers=headers, data=json.dumps(data))
    record = json.loads(response.text)
    return record
