import xmlrpc.client

#odoo Server Information
url = "http://localhost:7750"
db = "odoo-training"
username = "admin"
password = "admin"

# Common endpoint
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))

# Authenticate
uid = common.authenticate(db, username, password, {})
if uid:
    print(f"Logged in as {username} (uid: {uid})")

models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')
# Search records if is_company == true return 2 records from 3rd index
record_ids = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', True]]], {'offset': 3, 'limit': 2})

# Read 3 fields from each records
records = models.execute_kw(db, uid, password, 'res.partner', 'read', [record_ids, ['name', 'country_id', 'comment']])
print(records)

#create record
new_record_id = models.execute_kw(db, uid, password, 'res.partner', 'create', [{
    'name': "spiridian",
    'email': "spiridian@gmail.com",
    'is_company': True,
}])
d = models.execute_kw(db, uid, password, 'res.partner', 'read', [[new_record_id], ['display_name']])
print(f"Created record ID: {new_record_id}{d}")


#write
update_record = models.execute_kw(db, uid, password, 'res.partner', 'write', [[new_record_id], {
    'email': "newspridia@company.com",
}])
print("Record updated.")

#unlink
remove_record = models.execute_kw(db, uid, password, 'res.partner', 'unlink', [[new_record_id]])
s =models.execute_kw(db, uid, password, 'res.partner', 'search', [[['id', '=', new_record_id]]])
print('deleted',s)

print('return selected fields based search parameter')
record1 = models.execute_kw(db, uid, password, 'res.partner', 'search_read', [[['is_company', '=', True]]], {'fields': ['name', 'country_id', 'comment'], 'limit': 5})
print(record1)


list_record = models.execute_kw(db, uid, password, 'res.partner', 'fields_get', [], {'attributes': ['string', 'help', 'type']})
print('list record ....',list_record)



