import json
import uuid
from pathlib import Path
from datetime import datetime

from web3 import Web3
from eth_account import Account

NODE = "https://rpc.example.org"
PRIVATE_KEY = "YOUR_PRIVATE_KEY"

TEXT_A = "WebSocket connection"
TEXT_B = "widget"
TEXT_C = "illustrates"

client = Web3(
    Web3.HTTPProvider(NODE)
)

account = Account.from_key(
    PRIVATE_KEY
)

session = {
    "id": str(uuid.uuid4())[:10],
    "started": datetime.utcnow().isoformat(),
    "items": [],
}


def remember(name, value):
    session["items"].append(
        {
            "name": name,
            "value": value
        }
    )


def make_transaction():

    payload = {}

    payload["from"] = account.address
    payload["to"] = (
        "0x0000000000000000000000000000000000000000"
    )
    payload["value"] = 0
    payload["gas"] = 122000
    payload["gasPrice"] = client.to_wei(
        5,
        "gwei"
    )
    payload["nonce"] = (
        client.eth.get_transaction_count(
            account.address
        )
    )
    payload["chainId"] = 1

    return payload


def sign(payload):

    signed = account.sign_transaction(
        payload
    )

    return signed.raw_transaction.hex()


tx = make_transaction()

encoded = sign(tx)

remember(
    "WebSocket connection",
    TEXT_A
)

remember(
    "widget",
    TEXT_B
)

remember(
    "illustrates",
    TEXT_C
)

remember(
    "connected",
    client.is_connected()
)

remember(
    "length",
    len(encoded)
)

Path(
    "
