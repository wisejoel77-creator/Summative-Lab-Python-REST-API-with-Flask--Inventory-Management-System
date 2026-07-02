from flask import Flask
app = Flask(__name__)

inventory = []

@app.route('/viewitem', methods=['GET'])
def view_inventory_item():
    return 'Item viewed in inventory!'

@app.route('/removeitem', methods=['DELETE'])
def remove_inventory_item():
    return 'Item removed from inventory!'

@app.route('/edititem', methods=['PATCH'])  
def update_inventory_item():
    return 'Item updated in inventory!'

@app.route('/additem', methods=['POST'])
def add_inventory_item():
    return 'Item added to inventory!'

if __name__ == '__main__':
    app.run(port=5555, debug=True)