from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# @app.route('/payment/initiate', methods=['POST'])
# def initiate_payment():
#     # Get the JSON payload from the request
#     request_payload = request.get_json()

#     # Access the values from the payload
#     value_in_usd = request_payload.get('valueInUSD')
#     payer_email = request_payload.get('payerEmail')
#     currency = request_payload.get('currency')
#     amount = request_payload.get('amount')
#     redirect_url = request_payload.get('redirect_url')

#     # Simulate the Chimoney API response
#     response = {
#         "status": "success",
#         "message": "Payment initiated successfully",
#         "valueInUSD": value_in_usd,
#         "payerEmail": payer_email,
#         "currency": currency,
#         "amount": amount,
#         "redirect_url": redirect_url
#     }

#     return jsonify(response)


@app.route('/', methods = ["POST"])
def home():
    return "Hello World"

@app.route('/payment/initiate', methods = ["POST"])
def bvn_verification():
    try:
        # Get the JSON payload from the request
        # request_payload = request.get_json()

        # Access the values from the payload
        # value_in_usd = request_payload.get('valueInUSD')
        # payer_email = request_payload.get('payerEmail')
        # currency = request_payload.get('currency')
        # amount = request_payload.get('amount')
        # redirect_url = request_payload.get('redirect_url')


        url = "https://api-v2-sandbox.chimoney.io/v0.2/payment/initiate"

        payload = {
            "valueInUSD": 100,
            "payerEmail": "ogungbolamayowa@gmail.com",
            "currency": "NGN",
            "amount": "10",
            "redirect_url": "https://www.linkedin.com/feed/?nis=true&&lipi=urn%3Ali%3Apage%3Ad_flagship3_notifications%3BZc4DqQVrSd6UtszozgIvVQ%3D%3D"
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "X-API-KEY": "8fab3b70b9c800b0b16881f8f7c061af0d50ecd46956615e16f9b56664b9393a"
            # "X-API-KEY": "821ae70751f3e07be57a887ad61823b39c9faf1211c72d6ba62e2661d752b8da"
        }

        response = requests.post(url, json=payload, headers=headers)

        print(response.text)
        

#      response = requests.post(url, headers=headers, json=data)
        response_data = response.json()


        return jsonify(response_data)
    except Exception as e:
    # Handle exceptions, e.g., connection errors, request errors, etc.

        return (e)
    

@app.route('/payment/verify', methods = ["POST"])
def verify_payment():
    url = "https://api-v2-sandbox.chimoney.io/v0.2/payment/verify"
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "X-API-KEY": "821ae70751f3e07be57a887ad61823b39c9faf1211c72d6ba62e2661d752b8da"
    }
    payload = {
        "id": "DD73z2GXyWU4DuvJeRKGoHEoLFN2_100_1702406095792"
        # "id": "PhazoiV7gIZdbCVf1fskYFqUepq2_100_1702407560647"
    }
    
    try:

        response = requests.post(url, json=payload, headers=headers)

        print(response.text)
        

        response_data = response.json()
        return jsonify(response_data)
    except Exception as e:

        return (e)


if __name__ == '__main__':
    app.run(debug=True)
