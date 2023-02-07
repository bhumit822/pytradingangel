
from smartapi.smartConnect import SmartConnect
import pyotp
import time
import csv

from fivemindata import fiveMin
f = open("myfile.csv", "w")
cw = csv.writer(f)
cw.writerow(["TIME", "O", "H", "L", "C", 'Cm.V',
             'Nm.V', 'NNm.V', 'AllVolume'])

totp = pyotp.TOTP('7C5TSC67UH6OJW32MTFYTVTX7Q')
obj = SmartConnect(api_key="WrCFHEDN")
print(totp.now())
data = obj.generateSession("B73943", "9933", totp.now())
print(data["data"]['clientcode'])
print(data["data"]['name'])
# print(data)
refreshToken = data['data']['refreshToken']

# # #fetch the feedtoken
feedToken = obj.getfeedToken()

print(feedToken)

# # #fetch User Profile
userProfile = obj.getProfile(refreshToken)
# {"token": "26009", "symbol": "BANKNIFTY", "name": "BANKNIFTY", "expiry": "", "strike": "-1.000000",
#     "lotsize": "-1", "instrumenttype": "", "exch_seg": "NSE", "tick_size": "-1.000000"}
lll = obj.ltpData("NFO", "BANKNIFTY", "48756")
print(lll)
# # Place Order
# # try:
# #     orderparams = {
# #         "variety": "NORMAL",
# #         "tradingsymbol": "SBIN-EQ",
# #         "symboltoken": "3045",
# #         "transactiontype": "BUY",
# #         "exchange": "NSE",
# #         "ordertype": "LIMIT",
# #         "producttype": "INTRADAY",
# #         "duration": "DAY",
# #         "price": "19500",
# #         "squareoff": "0",
# #         "stoploss": "0",
# #         "quantity": "1"
# #         }
# #     orderId=obj.placeOrder(orderparams)
# #     print("The order id is: {}".format(orderId))
# # except Exception as e:
# #     print("Order placement failed: {}".format(e.message))


try:
    index = {
        "exchange": "NSE",
        "symboltoken": "26009",
        "interval": "FIVE_MINUTE",
        "fromdate": "2023-02-07 09:15",
        "todate": "2023-02-07 15:31"
    }
    historicParam = {
        "exchange": "NFO",
        "symboltoken": "48756",
        "interval": "FIVE_MINUTE",
        "fromdate": "2023-02-07 09:15",
        "todate": "2023-02-07 15:31"
    }
    historicParam1 = {
        "exchange": "NFO",
        "symboltoken": "37833",
        "interval": "FIVE_MINUTE",
        "fromdate": "2023-02-07 09:15",
        "todate": "2023-02-07 15:31"
    }
    historicParam2 = {
        "exchange": "NFO",
        "symboltoken": "35018",
        "interval": "FIVE_MINUTE",
        "fromdate": "2023-02-07 09:15",
        "todate": "2023-02-07 15:31"
    }
    # historicParam = {
    #     "exchange": "CDS",
    #     "name": "NIFTYFUTM1",
    #     "symbol": "NIFTYFUTURESNEARMONTH",
    #     "symboltoken": "5",
    #     "interval": "ONE_MINUTE",
    #     "fromdate": "2023-01-31 09:00",
    #     "todate": "2023-01-31 09:40"
    # }
    # indexprice = obj.getCandleData(index)
    data = obj.getCandleData(historicParam)
    # data1 = obj.getCandleData(historicParam1)
    # data2 = obj.getCandleData(historicParam2)
    # print(data)
    fiveMin(data['data'])
    for g in data['data']:
        cw.writerow(g)


except Exception as e:
    print("Historic Api failed: {}".format(e.message))

# historicParam = {
#     "exchange": "NSE",
#     "symboltoken": "3045",
#     "interval": "FIVE_MINUTE",
#     "fromdate": "2022-12-15 09:00",
#     "todate": "2022-12-15 15:16"
# }

# data = obj.getCandleData(historicParam)
# print(data)
