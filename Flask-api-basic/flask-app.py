from flask import Flask, jsonify, request
from db import shops,products
import uuid

app = Flask(__name__)


# ----> Shops data 


#--get

@app.route("/getshop", methods=["GET"])
def get_shops():#getting all the shops
    return jsonify(list(shops.values())), 200

@app.route("/shop/<shopid>", methods=["GET"])
def get_shop_by_id(shopid):#finding shop using shop ID
    for i in shops:
        if i==shopid:
            return jsonify({"Data":shops[i]}),200
    return jsonify({"message":"Data Not Found!"}),400

#--create (post)


@app.route("/createshop", methods=["POST"])
def create_shops():#creating the shops
    data = request.json
    if data:
        shopid=uuid.uuid4().hex
        shop={**data,"id":shopid}
        shops[shopid]=shop
        return shop, 201
    return jsonify({"message": "Invalid Data"}), 400

#--delete 


@app.route("/shop/<shopid>", methods=["DELETE"])
def del_shop(shopid):# deleting the shop using shop ID
    try:
        del shops[shopid]
        return jsonify({"message":"Shop Deleted"}),200
    except KeyError:
        return jsonify({"message":"Data not found"}),404

#--updating 

@app.route("/update_shop/<shopid>",methods=["PUT"])
def update_shop(shopid):#updating the shop using shop id 
    update=request.json
    try:
        shops[shopid]|=update
        return jsonify({"message":"Data updated successfully"}),200
    except KeyError:
        return jsonify({"message":"Data Not Found!"}),404



#----> Products data 



#--getting  

@app.route("/getproduct", methods=["GET"])
def get_product():#getting all the products
    return jsonify(list(products.values())), 200

@app.route("/product/<productid>", methods=["GET"])
def get_product_by_id(productid):#finding product using product ID
    for i in products:
        if i==productid:
            return jsonify({"Data":products[i]}),200
    return jsonify({"message":"Data Not Found!"}),400


#--creating(post)

@app.route("/createproduct", methods=["POST"])
def create_product():#creating the product
    product= request.json
    if product:
        if "shop_id" in product and product["shop_id"] in shops:
            product_id=uuid.uuid4().hex
            p={**product,"Product_id":product_id}
            products[product_id]=p
            return p,201
        return jsonify({"message":"NOt found "}),404
    return jsonify({"message":"Cannt Add product"}),400
    

#--deleting

@app.route("/product/<productid>", methods=["DELETE"])
def del_product(productid):# deleting the product using product ID
    try:
        del products[productid]
        return jsonify({"message":"Product Deleted"}),200
    except KeyError:
        return jsonify({"message":"Data not found"}),404


#--updating

@app.route("/update_product/<productid>",methods=["PUT"])
def update_product(productid):#updating the product using product id 
    update=request.json
    try:
        products[productid]|=update
        return jsonify({"message":"Data updated successfully"}),200
    except KeyError:
        return jsonify({"message":"Data Not Found!"}),404



if __name__ == "__main__":
    app.run(debug=True)