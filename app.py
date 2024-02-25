
from flask import Flask, render_template, jsonify, request
import json
import requests
import re

app = Flask(__name__)
import re

def strip_money(monies):
    if monies is None:
        return
    elif "." in monies:
        just_nums = re.sub(r'[^0-9.]', '', monies)
        just_nums = int(float(just_nums))
    else:
        just_nums = re.sub(r'[^0-9]', '', monies)
        just_nums = int(just_nums)
    return just_nums


def json_add(key, value, data=None):
    if data is None:
        data = []
    data_to_add = {key:value}
    try:
        with open('data.json', 'r') as json_file:
            old_data = json.load(json_file)
    except (FileNotFoundError, json.JSONDecodeError):
        old_data = []
    data.extend(old_data)
    data.append(data_to_add)
    with open('data.json', 'w') as json_file:
        json.dump(data, json_file, indent=2)
        json_file.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/credit', methods=['POST'])
def credit():
    credit_score = request.form.get('credit')
    print(credit_score)
    json_add('credit score', credit_score)
    return render_template('index.html',credit_score=credit_score)

@app.route('/client_name', methods=['POST'])
def client_name():

    client_name = request.form.get('client_name')
    print(client_name)
    json_add('client name', client_name)

    return render_template('index.html', client_name=client_name)

@app.route('/purch_price_and_down', methods=['POST'])
def purch_price_and_down():
    purchase_price = request.form.get("max_purch_price")
    print(purchase_price)
    purchase_price = strip_money(purchase_price)
    print(purchase_price)

    #json_add('purchase price', purchase_price)

    return render_template('index.html', purchase_price=purchase_price)

@app.route('/down', methods=['POST'])
def down():
    purchase_price = request.form.get("purchase_price")
    print(purchase_price)
    down_payment_type = request.form.get('down_payment_type')
    json_add('down payment type', down_payment_type)
    print(down_payment_type)
    down = request.form.get('down_pmnt')
    down = int(strip_money(down))
    if down_payment_type == 'percent':
        down_percent = int(down)
        down = int(purchase_price) * (down * .01)
        print(down)
        json_add('down payment', int(down))
    elif down_payment_type == 'dollars':
        down_percent = (int(down) / int(purchase_price)) * 100
        print(down_percent)
        json_add('down payment', int(down))
    json_add('purchase price', purchase_price)

    return render_template('index.html', purchase_price=purchase_price, down=down, down_percent=down_percent )

@app.route('/income', methods=['POST'])
def income():
    monthly = 0
    amount = request.form.get('amount')
    amount = int(amount)
    print(type(amount))
    income_type =  request.form.get('income')
    if income_type == 'year':
        monthly = amount / 12
    elif income_type == 'hour':
        monthly = ((amount * 40) * 50) / 12
    else:
        monthly = amount

    return render_template('index.html', income_amount = monthly)


@app.route('/to_API', methods=['GET'])
def to_API():
    with open('data.json','r') as json_file:
        data = json_file.readlines()

    data_list = [json.loads(entry) for entry in data]

    API_endpoint = 'https://mortgageapi.zillow.com/getRates'
    response = requests.post(API_endpoint, json=data_list)
    return jsonify({'status':'success', 'api_response': response.text})

@app.route('/debt', methods=['POST'])
def debt():
    card1 = request.form.get("credit_card1")
    card2 = request.form.get("credit_card2")
    card3 = request.form.get("credit_card3")
    card4 = request.form.get("credit_card4")
    card5 = request.form.get("credit_card5")
    card6 = request.form.get("credit_card6")
    if card1 is not None:
        card1 = strip_money(card1)
    else:
        card1 = 0
    if card2 is not None:
        card2 = strip_money(card2)
    else:
        card2 = 0
    if card3 is not None:
        card3 = strip_money(card3)
    else:
        card3 = 0
    if card4 is not None:
        card4 = strip_money(card4)
    else:
        card4 = 0
    if card5 is not None:
        card5 = strip_money(card5)
    else:
        card5 = 0
    if card6 is not None:
        card6 = strip_money(card6)
    else:
        card6 = 0

    cc_debt = []
    cc_debt.append(card1,card2,card3,card4,card5,card6)
    credit_card_debt = sum(cc_debt)

# create an array/dict and append to it with each submission, then return sum of the responses to have an updating amount
    # as we go instead of a limited number of cards

    return render_template('index.html', credit_card_debt=credit_card_debt)


if __name__ == '__main__':
    app.run(debug=True)



# break this down into chunks.  Store the values entered in each chunk as variables (maybe even upon entering) and
# then pass it to python to calculate and store, then send back to the rendered html for display.  Copy and paste the
# html code into each page so the form turns into the just displayed text, but store it to a Json file for printing
# and calling microservice.  See "python programming" on youtube for good tutorials