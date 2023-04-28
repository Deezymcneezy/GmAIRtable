import requests
import json

def get_airtable_records(api_key, base_id, table_name):
    headers = {
        'Authorization': 'Bearer ' + api_key,
    }
    url = f'https://api.airtable.com/v0/{base_id}/{table_name}'
    response = requests.get(url, headers=headers)
    records = json.loads(response.text)['records']
    return records
