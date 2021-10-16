import requests
from flask import Flask

#########HTML FORMAT USED IN PYTHON CODE ############
template = """<!DOCTYPE html>
<html>
<head>
<title>
Bitcoin
</title>
</head>
<body>
<h1 style="text-align:center">
BITCOIN --> USD ($) CONVERTER
</h1>
<p>
Welcome!! this app is here to help people who would like to purchase bitcoins.
here you can check the value of Bitcoin in USD ($).
you can also check the average value of Bitcoin in USD in the last 10 minutes
</p>
<h2>
To buy one BTC (BitCoin) in USD it would cost you:
$$replace_this1$$
</h2>
<h2>
The price of BTC is forever changing, here is the average of its value in USD over the last 10 minutes:
$$replace_this2$$
</h2>
<img src="https://thumbor.forbes.com/thumbor/960x0/https%3A%2F%2Fspecials-images.forbesimg.com%2Fdam%2Fimageserve%2F908633080%2F960x0.jpg%3Ffit%3Dscale" width="250" height="150">
</body>
</html>"""
########## END OF HTML FORMAT IN PYTHON ##########

app = Flask(__name__)

## the api used is cryptocompare:
URL = "https://min-api.cryptocompare.com/data/v2/histominute?fsym={}&tsym={}&limit={}"


##function to calculate its value from the given API
def get_price(coin,currency,limit):
    sum = 0
    try:
        response = requests.get(URL.format(coin,currency,limit)).json()
        for i in range(10):
            sum += response['Data']['Data'][i]['close']
        return response['Data']['Data'][9]['close'],sum/10
    except:
        return False

##to enter the website we used app.route
@app.route("/")
def hello_world():
    currentprice,average= get_price("BTC","USD","10")
    html_result = template.replace("$$replace_this1$$", str(currentprice))
    html_result = html_result.replace("$$replace_this2$$",str(average))
    return html_result

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80)
###running on port 80
