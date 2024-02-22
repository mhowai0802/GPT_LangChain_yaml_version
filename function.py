import os
import requests
import json
from waitress import serve
from flask import Flask, request, jsonify, send_from_directory


class function_route():

  def __init__(self, apikey):

    self.apikey_apilayer = apikey['apikey_apilayer']
    self.apikey_eden = apikey['apikey_eden']

  def get_exchange_rate(self, from_currency, to_currency, amount, date=None):

    url = f"https://api.apilayer.com/exchangerates_data/convert?from={from_currency}&to={to_currency}&amount={amount}"
    headers = {"apikey": self.apikey_apilayer}
    response = requests.get(url, headers=headers)
    print(response.json())
    return response.json()

# Global variables
app = Flask(__name__)
apikey = {
  "apikey_apilayer": os.environ['Authorization_apilayer'],
  "apikey_eden": os.environ['Authorization_eden']
}
function_object = function_route(apikey)


# Routing Http requests
@app.route('/convert', methods=['GET'])
def convert_currency():
  from_currency = request.args.get('from')
  to_currency = request.args.get('to')
  amount = request.args.get('amount')
  date = request.args.get('date', None)
  try:
    converted_amount = function_object.get_exchange_rate(
      from_currency, to_currency, amount, date)
    return jsonify({
      "from": from_currency,
      "to": to_currency,
      "amount": amount,
      "converted_amount": converted_amount
    })
  except Exception as e:
    return jsonify({"error": str(e)}), 400


# Refer to the configuration documents
@app.route('/.well-known/ai-plugin.json')
def serve_ai_plugin():
  return send_from_directory('.',
                             'ai-plugin.json',
                             mimetype='application/json')


@app.route('/.well-known/openapi.yaml')
def serve_openapi_yaml():
  return send_from_directory('.', 'openapi.yaml', mimetype='text/yaml')


if __name__ == '__main__':
  serve(app, host="0.0.0.0", port=8080)
