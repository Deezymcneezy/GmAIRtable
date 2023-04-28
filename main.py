from airtable_query import find_airtable_records
from airtable_create import create_airtable_record
from airtable_update import update_airtable_record
from airtable_delete import delete_airtable_record

# Replace with your own Airtable API key, base ID, and table name
api_key = 'YOUR_API_KEY'
base_id = 'YOUR_BASE_ID'
table_name = 'YOUR_TABLE_NAME'

# Example usage: find records
records = find_airtable_records(api_key, base_id, table_name, max_records=10)
print(records)

# Example usage: create a record
fields = {
    'Name': 'John Doe',
    'Email': 'john.doe@example.com',
    'Phone': '555-555-5555'
}
record = create_airtable_record(api_key, base_id, table_name, fields)
print(record)

# Example usage: update a record
record_id = 'rec123'
fields = {
    'Name': 'Jane Doe',
    'Email': 'jane.doe@example.com',
    'Phone': '555-123-4567'
}
record = update_airtable_record(api_key, base_id, table_name, record_id, fields)
print(record)

# Example usage: delete a record
record_id = 'rec123'
success = delete_airtable_record(api_key, base_id, table_name, record_id)
print(success)
