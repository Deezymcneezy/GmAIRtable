import requests

def delete_airtable_record(api_key, base_id, table_name, record_id):
    headers = {
        'Authorization': 'Bearer ' + api_key
    }
    url = f'https://api.airtable.com/v0/{base_id}/{table_name}/{record_id}'
    response = requests.delete(url, headers=headers)
    return response.status_code == 200
