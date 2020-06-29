# Stripe Payment Intent Integration: Corgi Merch 

Corgi Merch site that accepts one-time payments for purchases of a corgi button.

Forked from Stripe sample app here: https://github.com/stripe-samples/react-elements-card-payment

## App Features

Two product types are offered: Eclair button and Beignet button. Users can choose between the two products and then initiate a card payment. 

This application incudes a `client` in React and a `server` in Python.

## How to run locally

To run this application locally you need to start both a local dev server for the `front-end` and another server for the `back-end`.

You will need a Stripe account with its own set of [API keys](https://stripe.com/docs/development#api-keys).

Follow the steps below to run locally.

1. Clone the repository: 

```
git clone https://github.com/fangKfang/corgi-merch-stripe.git
```

2. You will need a Stripe account in order to run the application. Once you set up your account, go to the Stripe [developer dashboard](https://stripe.com/docs/development#api-keys) to find your API keys. 

3. Copy the `.env.example` file into a file named `.env` into `./server` folder. Update your `.env` file with your Stripe API keys. 

```
STRIPE_PUBLISHABLE_KEY=<replace-with-your-publishable-key>
STRIPE_SECRET_KEY=<replace-with-your-secret-key>
```
## Running the application

Assuming you are using a Mac, install the following:

* Download Firefox: https://www.mozilla.org/en-US/firefox/new/
* Download the CORS Everywhere extension for Firefox: https://addons.mozilla.org/en-US/firefox/addon/cors-everywhere/. You will need this extension in order to manage requests between the API server and the React client. 
* Download [Homebrew](https://brew.sh/) or your favorite package manager to install the latest versions of: 
- Python 3 
- Pip 
- Yarn
- Node 
- NPM 

**Optional:**
Install Stripe CLI by following the [installation steps](https://github.com/stripe/stripe-cli#installation). The Stripe CLI is needed for locally testing webhooks.

### Running the API server

1. Go to `/server`
2. Run `python server.py`
3. Go to http://127.0.0.1:4242/ to check that the server is running. 


### Running the React client

1. Go to `/client`
3. Run `yarn`
3. Run `yarn start` 
4. Go to http://127.0.0.1:3000/ using Firefox to see your application. Ensure the CORS Everywehre extension is turned on. 

### Using the app

1. Select the corgi button you want to purchase
2. Enter your name and card details
2. Hit "Pay"

## Use the Stripe CLI to test webhooks

You can use the Stripe CLI to run a webhook locally. 

First install the Stripe CLI and ensure your Stripe account is linked. 

The CLI will print a webhook secret key to the console. Set STRIPE_WEBHOOK_SECRET to this value in your `.env` file.

Then enter the following in your console:
```
stripe listen -f 127.0.0.1:4242/webhook
```
Use the applicaiton. You should see events logged in the console where the CLI is running. Additionally, every payload from `payment_intent.succeeded` webhook event will be logged to the `purchases.log` file. 
