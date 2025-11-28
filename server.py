from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Backend is running"

@app.route("/pools/<dex>")
def get_pools(dex):
    pools = [
        {
            "pair": "ETH/USDT",
            "pairAddress": "0x123",
            "tvl": 1234567,
            "volume24h": 234567,
            "feeTvl": 1.23,
            "apr": 450,
            "volatility": 2.5,
            "sparkline": [1, 2, 3, 4, 5, 6]
        },
        {
            "pair": "BTC/USDT",
            "pairAddress": "0x456",
            "tvl": 2345678,
            "volume24h": 345678,
            "feeTvl": 0.98,
            "apr": 360,
            "volatility": 3.1,
            "sparkline": [2, 3, 4, 5, 6, 7]
        }
    ]
    return jsonify(pools)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
