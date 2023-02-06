

from smartapi import SmartWebSocket
from index import h
# feed_token=092017047
FEED_TOKEN = "0823485347"
CLIENT_CODE = "B73943"
# token = "mcx_fo|224395"
token = "nse_cm|2885"
# token="mcx_fo|226745&mcx_fo|220822&mcx_fo|227182&mcx_fo|221599"
task = "sfi"
ss = SmartWebSocket(FEED_TOKEN, CLIENT_CODE)


def on_message(ws, message):
    h()
    print("Ticks: {}".format(message))


def on_open(ws):
    print("on open")
    ss.subscribe(task, token)


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("Close")


# Assign the callbacks.
ss._on_open = on_open
ss._on_message = on_message
ss._on_error = on_error
ss._on_close = on_close

ss.connect()
