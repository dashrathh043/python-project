import json
from flask import Flask,jsonify
import os
import pathlib
parent_dir = pathlib.Path(__file__).parent.resolve()
json_path = os.path.join(parent_dir,'products.json')

# Read JSON file
with open(json_path) as fp:
    products = json.load(fp)

app = Flask(__name__)

#root
@app.route('/')
def index():
    return "<h1><=========== Welcome to REST API ===================></h1>"

#list-of-all-products
@app.route("/products", methods=['GET'])
def get():
    return jsonify(products)


#get-product-by-ID
@app.route("/products/<int:id>", methods=['GET'])
def get_product_by_id(id):
    return jsonify(products[id])


#add-product
#curl -i -H "Content-Type:Application/json" -X POST http://127.0.0.1:5000/products
@app.route("/products", methods=['POST'])
def add_product():
    products.append({
        "id":5,
        "name":"Redmi 100 cm (32 inches) HD Ready Smart LED TV | L32M6-RA (Black) (2021 Model) | With Android 11",
        "price":"25,999"
    })
    # update the JSON file
    with open(json_path, 'w') as j_file:
        json.dump(products, j_file, indent=4, separators=(',',': '))
    return jsonify(products)


#update
#curl -i -H "Content-Type:Application/json" -X PUT http://127.0.0.1:5000/products
@app.route("/products/<int:id>",methods=['PUT'])
def update_product(id):
    products[id]['name'] = "New-Name"
     # update the JSON file
    with open(json_path, 'w') as j_file:
        json.dump(products, j_file, indent=4, separators=(',',': '))
    return jsonify(products)



#delete
#curl -i -H "Content-Type:Application/json" -X DELETE http://127.0.0.1:5000/products
@app.route("/products/<int:id>",methods=['DELETE'])
def delete(id):
    products.remove(products[id])
     # update the JSON file
    with open(json_path, 'w') as j_file:
        json.dump(products, j_file, indent=4, separators=(',',': '))
    return jsonify(products)



if __name__ == "__main__":
    app.run(debug = True)
