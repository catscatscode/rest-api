from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'ScrappleStore',
        'items': [
            {
                'name': 'MyPad',
                'price': 150.99
            }
        ]
    }
]

# GET: view all stores
@app.route('/stores')
def get_all_stores():
    # made the stores variable (a list) into a dict before passing it into jsonify,
    # because json cannot be a list
    return jsonify({'stores': stores})

# GET: view a store
@app.route('/stores/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})

# GET: view all items from a store
@app.route('/stores/<string:name>/items')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found'})

# POST: add a new store
@app.route('/stores', methods=['POST'])
def create_store():
    request_data = request.get_json() # gets json and converts it into a python dict
    new_store = {
        'name': request_data['name'], # retrieve from dict's key-value pair
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store) # convert dict into json/str before returning to client

# POST: add a new item with its price to an existing store
@app.route('/stores/<string:name>/item', methods=['POST'])
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(store)
    return jsonify({'message': 'store not found'})

app.run(debug=True)
