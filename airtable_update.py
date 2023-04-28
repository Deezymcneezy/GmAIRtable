import requests
import json

def update_airtable_record(api_key, base_id, table_name, record_id, fields):
    headers = {
        'Authorization': 'Bearer ' + api_key,
        'Content-Type': 'application/json'
    }
    data = {
        'fields': fields
    }
    url = f'https://api.airtable.com/v0/{base_id}/{table_name}/{record_id}'
    response = requests.patch(url, headers=headers, data=json.dumps(data))
    record = json.loads(response.text)
    return record
