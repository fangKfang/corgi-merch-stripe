# Stripe Payment Intent Integration: Corgi Merch 

Corgi Merch site that accepts a payment for purchases of a corgi button using the [Payment Intents API](https://stripe.com/docs/payments/payment-intents), [Stripe Elements](https://stripe.com/payments/elements) and [React](https://reactjs.org/).

## Features

Two product types are offered: Eclair button and Beignet button. Users can choose between the two products and then initiate a card payment. 

This sample consists of a `client` in React and a `server` in Python.

## How to run locally

To run this application locally you need to start both a local dev server for the `front-end` and another server for the `back-end`.

You will need a Stripe account with its own set of [API keys](https://stripe.com/docs/development#api-keys).

Follow the steps below to run locally.

**Installing and cloning manually**

Clone the repository: 

```
git clone https://github.com/fangKfang/corgi-merch-stripe.git
```
You will need a Stripe account in order to run the application. Once you set up your account, go to the Stripe [developer dashboard](https://stripe.com/docs/development#api-keys) to find your API keys.

```
STRIPE_PUBLISHABLE_KEY=<replace-with-your-publishable-key>
STRIPE_SECRET_KEY=<replace-with-your-secret-key>
```
## Running the application

Prerequeistes: 
* Download Firefox: https://www.mozilla.org/en-US/firefox/new/
* Download the CORS Everywhere extension: https://addons.mozilla.org/en-US/firefox/addon/cors-everywhere/. You will need this in order to manage requests between the API server and the React client. 
* Install Python 3 
* Install Pip 
* Install Node 
* Install NPM 
* Install Stripe CLI: Follow the [installation steps](https://github.com/stripe/stripe-cli#installation). The CLI is needed for locally testing webhooks and Stripe integrations.

### Running the API server

1. Go to `/server`
2. `python server.py`f

### Running the React client

1. Go to `/client`
3. Run `yarn`
3. Run `yarn start` and go to http://127.0.0.1:3000/ using Firefox. 

### Using the sample app

1. Enter your name and card details

## Use the Stripe CLI to test webhooks
