#! /usr/bin/env python3.6

"""
server.py
Stripe Recipe.
Python 3.6 or newer required.
"""

import logging
import stripe
import json
import os

from flask import Flask, render_template, jsonify, request, send_from_directory
from dotenv import load_dotenv, find_dotenv

app = Flask(__name__, static_url_path="")

logging.basicConfig(level=logging.ERROR, filename='purchases.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
# Setup Stripe python client library
load_dotenv(find_dotenv())
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')
stripe.api_version = os.getenv('STRIPE_API_VERSION')
product_list = [{
                'id':'1',
                'name':'Eclair', 
                'price':'1000', 
                'currency':'EUR',
                'img':'https://i.ibb.co/hZg1NZc/eclair-button.jpg'
                },
                {
                'id':'2',
                'name':'Beignet', 
                'price':'800', 
                'currency':'USD',
                'img':'https://i.ibb.co/DGXj74H/beignet-button.jpg'
                },
            ]

def default_product_details():
  return {
    'currency': 'USD',
    'amount': 51
  }

@app.route('/', methods=['GET'])
def home():
    return "Hello from API!"

@app.route('/products', methods=['GET'])
def products():
    return jsonify(product_list)

@app.route('/public-key', methods=['GET'])
def PUBLISHABLE_KEY():
    return jsonify({
        'publicKey': os.getenv('STRIPE_PUBLISHABLE_KEY')
    })

@app.route('/product-details', methods=['GET'])
def get_product_details():
    product = product_details()
    return jsonify(product)

@app.route('/create-payment-intent', methods=['POST'])
def post_payment_intent():
    # Reads application/json and returns a response
    data = json.loads(request.data or '{}')
    product_id = data.pop('id', None)
    product = default_product_details()
    for item in product_list:
        if item['id'] == product_id:
            product['amount'] = item['price']
            product['currency'] = item['currency']
    options = dict()
    options.update(data)
    options.update(product)
    
    # Create a PaymentIntent with the order amount and currency
    payment_intent = stripe.PaymentIntent.create(
        **options,
        metadata={'integration_check': 'accept_a_payment'},
)

    try:
        return jsonify(payment_intent)
    except Exception as e:
        return jsonify(error=str(e)), 403

@app.route('/update-payment-intent', methods=['POST'])
def update-payment-intent():
    #When other product is selected, update existing payment intent 
    
    pass

@app.route('/purchases', methods=['POST'])
def store_purchase():
    purchase_data = json.loads(request.data or '{}')
    return jsonify({'something':''})


@app.route('/webhook', methods=['POST'])
def webhook_received():
    # Use webhooks to receive information about asynchronous payment events.
    webhook_secret = os.getenv('STRIPE_WEBHOOK_SECRET')
    request_data = json.loads(request.data)

    if webhook_secret:
        # Retrieve the event by verifying the signature using the raw body and secret if webhook signing is configured.
        signature = request.headers.get('stripe-signature')
        try:
            event = stripe.Webhook.construct_event(
                payload=request.data, sig_header=signature, secret=webhook_secret)
            data = event['data']
        except Exception as e:
            return e
        # Get the type of webhook event sent - used to check the status of PaymentIntents.
        event_type = event['type']
    else:
        data = request_data['data']
        event_type = request_data['type']
    data_object = data['object']
    
    print('event ' + event_type)

    if event_type == 'payment_intent.succeeded':
        logger.error(data_object)
        # Fulfill any orders, e-mail receipts, etc
        print("💰 Payment received!")

    if event_type == 'payment_intent.payment_failed':
        #Notify the customer that their order was not fulfilled
        print("❌ Payment failed.")

    return jsonify({'status': 'success'})


if __name__== '__main__':
    app.run(host='0.0.0.0', port=4242)
