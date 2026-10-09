from flask import Flask, jsonify, request
import requests
import os

app = Flask(__name__)

PRODUCT_SERVICE_URL = os.getenv(
    "PRODUCT_SERVICE_URL",
    "http://127.0.0.1:5000"
)

USER_SERVICE_URL = os.getenv(
    "USER_SERVICE_URL",
    "http://127.0.0.1:5001"
)

orders = []


@app.route("/orders", methods=["GET"])
def get_orders():
    return jsonify(orders)


@app.route("/orders", methods=["POST"])
def create_order():

    data = request.get_json()

    user_id = data.get("user_id")
    product_id = data.get("product_id")
    quantity = data.get("quantity")

    try:
        user_response = requests.get(
            f"{USER_SERVICE_URL}/users/{user_id}"
        )

        product_response = requests.get(
            f"{PRODUCT_SERVICE_URL}/products/{product_id}"
        )

        if user_response.status_code != 200:
            return jsonify({"error": "User not found"}), 404

        if product_response.status_code != 200:
            return jsonify({"error": "Product not found"}), 404

        user = user_response.json()
        product = product_response.json()

        total = product["price"] * quantity

        order = {
            "user_id": user_id,
            "user_name": user["name"],
            "product_id": product_id,
            "product_name": product["name"],
            "quantity": quantity,
            "total": total,
            "status": "Order created"
        }

        orders.append(order)

        return jsonify(order), 201

    except requests.exceptions.RequestException:
        return jsonify(
            {"error": "Unable to communicate with other services"}
        ), 500


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "Order Service is running"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
