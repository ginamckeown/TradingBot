# import ta-lib
import binance
# import numpy as np
import websocket
import json
import pprint
from twilio.rest import Client
import json
import urllib.request

# CONSTANTS
SOCKET = "wss://stream.binance.com:9443/ws/btcusdt@kline_1m"
closes = []


def on_open(ws):
    print("Opened Connection")


def on_close(ws):
    print("Closed Connection")


def on_message(ws, message):
    print("Recieved Message")
    json_message = json.loads(message)
    pprint.pprint(json_message)

    candle = json_message["k"]
    candle_closed = candle["x"]  # end of candle
    close = candle["c"]  # closing price

    if candle_closed:
        print("Candle closed at {}".format(close))
        closes.append(float(close))
        print("Closes:")
        print(closes)

def on_error(ws, error):
    print(error)


if __name__ == "__main__":
    ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message, on_error=on_error)
    ws.run_forever()
